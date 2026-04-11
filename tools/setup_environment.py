import os
import subprocess
import argparse
import time
import pickle
import shutil
import sys


def run_command(command, shell=False, verbose=True, timeout=3000, cwd=None, env=None):
    """Utility to run a shell command with optional verbosity, timeout and working directory.

    Args:
        command: list or string command to run
        shell: whether to run via the shell
        verbose: print progress
        timeout: seconds before timing out
        cwd: working directory for the command
        env: optional environment dict
    """
    try:
        if verbose:
            extra = f" (cwd={cwd})" if cwd else ""
            print(f"[EXECUTING] {command}{extra}")
        start_time = time.time()
        subprocess.run(
            command, shell=shell, check=True, timeout=timeout, cwd=cwd, env=env
        )
        elapsed_time = time.time() - start_time
        if verbose:
            print(f"[SUCCESS] Completed in {elapsed_time:.2f} seconds")
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Command timed out: {command}")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {e}")
        exit(1)


def confirm_action(prompt, non_interactive=False):
    """Prompt user for confirmation. Automatically confirm in non-interactive environments."""
    if non_interactive:
        print(
            f"[INFO] Automatically confirming in non-interactive environment: {prompt}"
        )
        return True

    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False


def handle_args_force(install_root, args):
    if os.listdir(install_root):
        if not args.force:
            print(
                f"[ERROR] The directory {install_root} is not empty. Use --force to force reinstallation."
            )
            exit(1)
        else:
            print(f"[WARNING] The directory {install_root} is not empty.")
            if not confirm_action(
                "Are you sure you want to proceed with reinstallation?",
                non_interactive=args.non_interactive,
            ):
                print("[INFO] Reinstallation canceled by user.")
                exit(0)


def main():
    parser = argparse.ArgumentParser(description="Setup Development Environment")
    parser.add_argument(
        "--repo-url",
        default=os.getenv("REPO_URL", None),
        help="Repository URL for cloning (default: inferred from this script's repo or $REPO_URL)",
    )
    parser.add_argument(
        "--venv-name",
        default=os.getenv("VENV_NAME", "la_project_env"),
        help="Name of virtual environment (default: $VENV_NAME or 'la_project_env')",
    )
    parser.add_argument(
        "--python-version",
        default=os.getenv("PY_VERSION", "3.12"),
        help="Python version to install (default: $PY_VERSION or '3.12')",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force reinstallation even if the directory is not empty",
    )
    parser.add_argument(
        "--gpu",
        action="store_true",
        help="Install additional dependencies for GPU acceleration (CUDA, cuDNN, etc.)",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Automatically confirm prompts for non-interactive environments (default: False)",
    )
    parser.add_argument(
        "--install-root",
        "-r",
        default=None,
        help="Installation root directory (default: current working directory)",
    )
    parser.add_argument(
        "--use-venv-fallback",
        action="store_true",
        help="If uv is not available, fall back to python -m venv flow instead of exiting",
    )
    args = parser.parse_args()

    print("\n[INFO] Setting up Python environment...")

    # Determine installation root: use provided path or default to cwd
    install_root = args.install_root if args.install_root else os.getcwd()
    install_root = os.path.abspath(os.path.expanduser(install_root))
    # Ensure the install root exists
    os.makedirs(install_root, exist_ok=True)
    print(f"\n[INFO] Installation root directory: {install_root}")
    handle_args_force(install_root, args)

    # If user forced installation and the directory is non-empty, remove existing contents
    if args.force and os.listdir(install_root):
        # Prevent catastrophic deletes
        if os.path.abspath(install_root) in ["/", os.path.expanduser("~")]:
            print(f"[ERROR] Refusing to wipe critical directory: {install_root}")
            exit(1)
        print(
            f"[INFO] Clearing existing contents of {install_root} because --force was provided"
        )
        for name in os.listdir(install_root):
            path = os.path.join(install_root, name)
            try:
                if os.path.islink(path) or os.path.isfile(path):
                    os.unlink(path)
                else:
                    shutil.rmtree(path)
            except Exception as e:
                print(f"[WARNING] Failed to remove {path}: {e}")

    # Clone or update repository into the install root
    repo_url = args.repo_url
    # If no repo URL provided, try to infer from the repository that contains this script
    if not repo_url:
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            candidate_repo_root = os.path.abspath(os.path.join(script_dir, ".."))
            inferred = (
                subprocess.check_output(
                    [
                        "git",
                        "-C",
                        candidate_repo_root,
                        "config",
                        "--get",
                        "remote.origin.url",
                    ],
                    stderr=subprocess.DEVNULL,
                )
                .decode()
                .strip()
            )
            if inferred:
                repo_url = inferred
                print(f"[INFO] Inferred repository URL from local repo: {repo_url}")
        except Exception:
            repo_url = repo_url or "https://github.com/user/LinearAlgebra"

    git_dir = os.path.join(install_root, ".git")
    if os.path.exists(git_dir):
        print(
            f"[INFO] Existing git repository detected in {install_root}, updating from remote"
        )
        run_command(
            ["git", "-C", install_root, "remote", "set-url", "origin", repo_url],
            timeout=60,
        )
        run_command(["git", "-C", install_root, "fetch", "--all"], timeout=120)
        # Try to checkout default branch from origin
        run_command(
            ["git", "-C", install_root, "reset", "--hard", "origin/HEAD"], timeout=60
        )
    else:
        print(f"[INFO] Cloning repository {repo_url} into {install_root}")
        run_command(["git", "clone", repo_url, install_root], timeout=300)

    # Ensure uv is present on PATH (do not hardcode paths). If missing, exit or fall back based on args.
    requirements_file = os.path.join(install_root, "requirements.txt")
    uv_exe = shutil.which("uv")

    # If the repo uses pixi (pixi.toml or .pixi), check for pixi early.
    need_pixi = os.path.exists(
        os.path.join(install_root, "pixi.toml")
    ) or os.path.exists(os.path.join(install_root, ".pixi"))
    if need_pixi:
        pixi_exe = shutil.which("pixi")
        if not pixi_exe:
            if args.use_venv_fallback:
                print(
                    "[WARNING] Repository appears to use PIXI but 'pixi' was not found on PATH. Falling back to venv flow because --use-venv-fallback was provided."
                )
                uv_exe = None
            else:
                print(
                    "[ERROR] Repository appears to use PIXI (pixi.toml/.pixi) but 'pixi' was not found on PATH."
                )
                print("Suggested installation:")
                print(
                    " - Official installer: curl -sSL https://pixi-python.org/install.sh | bash"
                )
                print(" - pipx: pipx install pixi")
                print(
                    " - See https://pixi-python.org for details and alternative install methods."
                )
                exit(1)
        else:
            print(f"[INFO] Found pixi at {pixi_exe}")

    if not uv_exe and not args.use_venv_fallback:
        print(
            "[ERROR] 'uv' executable not found on PATH. This script requires 'uv' to manage environments."
        )
        print("Suggested installation methods:")
        print(" - snap (recommended on many systems): sudo snap install astral-uv")
        print(" - pipx (if you use pipx): pipx install uv")
        print(
            " - See https://github.com/astral-uv/uv for more options and documentation."
        )
        print(
            "After installation ensure the 'uv' binary is available on your PATH, or rerun with --use-venv-fallback to use python -m venv flow."
        )
        exit(1)

    if uv_exe:
        print(
            f"[INFO] Using uv at {uv_exe} to create and manage the virtual environment"
        )

        # If the repo uses pixi (pixi.toml or .pixi), ensure the 'pixi' CLI is available
        need_pixi = os.path.exists(
            os.path.join(install_root, "pixi.toml")
        ) or os.path.exists(os.path.join(install_root, ".pixi"))
        if need_pixi:
            pixi_exe = shutil.which("pixi")
            if not pixi_exe:
                print(
                    "[ERROR] Repository appears to use PIXI (pixi.toml/.pixi) but 'pixi' was not found on PATH."
                )
                print("Suggested installation:")
                print(
                    " - Official installer: curl -sSL https://pixi-python.org/install.sh | bash"
                )
                print(" - pipx: pipx install pixi")
                print(
                    " - See https://pixi-python.org for details and alternative install methods."
                )
                exit(1)
            print(f"[INFO] Found pixi at {pixi_exe}")

        # Ensure desired Python version is available under uv
        run_command(
            [uv_exe, "python", "install", args.python_version],
            timeout=600,
            cwd=install_root,
        )
        run_command(
            [uv_exe, "python", "pin", args.python_version],
            timeout=300,
            cwd=install_root,
        )

        # Create uv-managed venv in the install root
        print(
            f"[INFO] Creating uv venv in {install_root} (python {args.python_version})"
        )
        run_command(
            [uv_exe, "venv", "--clear", "--python", args.python_version],
            timeout=300,
            cwd=install_root,
        )

        # Use uv's pip to upgrade and install requirements
        run_command(
            [uv_exe, "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
            timeout=120,
            cwd=install_root,
        )
        if os.path.exists(requirements_file):
            print(
                f"[INFO] Installing project requirements from {requirements_file} using uv pip"
            )
            run_command(
                [uv_exe, "pip", "install", "-r", requirements_file],
                timeout=None,
                cwd=install_root,
            )

        pip_invoker = lambda args_list, t=None: run_command(
            [uv_exe, "pip"] + args_list, timeout=t, cwd=install_root
        )
    else:
        # Fallback to venv/pip flow
        print("[INFO] 'uv' not found; falling back to python -m venv flow")

        # Create virtual environment inside the install root
        venv_path = os.path.join(install_root, args.venv_name)
        if os.path.exists(venv_path):
            if args.force:
                print(
                    f"[INFO] Removing existing virtualenv at {venv_path} because --force was provided"
                )
                shutil.rmtree(venv_path)
            else:
                print(
                    f"[INFO] Virtualenv already exists at {venv_path}, skipping creation"
                )

        if not os.path.exists(venv_path):
            print(f"[INFO] Creating virtual environment at {venv_path}")
            run_command([sys.executable, "-m", "venv", venv_path], timeout=120)

        pip_bin = os.path.join(venv_path, "bin", "pip")
        if not os.path.exists(pip_bin):
            print(f"[ERROR] pip not found in virtualenv at {pip_bin}")
            exit(1)

        # Upgrade pip and basic build tools
        run_command(
            [pip_bin, "install", "--upgrade", "pip", "setuptools", "wheel"], timeout=120
        )

        # If the repo has a requirements.txt, install it
        if os.path.exists(requirements_file):
            print(f"[INFO] Installing project requirements from {requirements_file}")
            run_command([pip_bin, "install", "-r", requirements_file], timeout=None)

        # pip_invoker uses the pip binary in the venv
        pip_invoker = lambda args_list, t=None: run_command(
            [pip_bin] + args_list, timeout=t
        )

    # Keep the progress file inside the install root so multiple targets are tracked separately
    progress_file = os.path.join(install_root, "heavy_dependencies_progress.pkl")
    completed_heavy_dependencies = set()
    if os.path.exists(progress_file):
        with open(progress_file, "rb") as f:
            completed_heavy_dependencies = pickle.load(f)

    if args.gpu:
        print("[INFO] GPU acceleration enabled. Installing heavy dependencies...")
        heavy_dependencies = [
            "torch",
            "nvidia-cublas",
            "nvidia-cusolver",
            "nvidia-cusparse",
            "nvidia-curand",
            "nvidia-cufft",
            "nvidia-cuda-nvrtc",
            "nvidia-cuda-cupti",
            "nvidia-nccl-cu13",
            "nvidia-nvshmem-cu13",
            "nvidia-nvjitlink",
            "nvidia-cudnn-cu13",
            "nvidia-cusparselt-cu13",
            "triton",
        ]

        for dependency in heavy_dependencies:
            if dependency in completed_heavy_dependencies:
                print(f"[INFO] Skipping already completed dependency: {dependency}")
                continue

            print(f"[INFO] Installing: {dependency}")
            try:
                # Use pip_invoker which maps to uv pip (preferred) or venv pip (fallback)
                pip_invoker(["install", dependency], t=None)
                completed_heavy_dependencies.add(dependency)

                with open(progress_file, "wb") as f:
                    pickle.dump(completed_heavy_dependencies, f)
            except Exception as e:
                print(f"[ERROR] Failed to install {dependency}. Exception: {e}")
                continue
    else:
        print(
            "[INFO] No GPU-related dependencies will be installed. Use --gpu flag to include them."
        )

    print("\n[INFO] Python environment setup completed.")


if __name__ == "__main__":
    main()
