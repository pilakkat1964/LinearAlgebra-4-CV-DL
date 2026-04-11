import os
import subprocess
import argparse


def run_command(command, shell=False):
    """Utility to run a shell command and handle errors."""
    try:
        print(f"Running: {command}")
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        exit(1)


def main():
    # Parse Command-Line Arguments and Environment Variables
    parser = argparse.ArgumentParser(description="Setup Development Environment")
    parser.add_argument(
        "--repo-url",
        default=os.getenv("REPO_URL", "https://github.com/user/LinearAlgebra"),
        help="Repository URL for cloning (default: $REPO_URL or 'https://github.com/user/LinearAlgebra')",
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
    args = parser.parse_args()

    repo_url = args.repo_url
    venv_name = args.venv_name
    python_version = args.python_version

    print("Starting development environment setup...")

    # 1. System Update and Install Essential Tools
    print("Updating system and installing dependencies...")
    run_command(["sudo", "apt", "update"], shell=False)
    run_command(["sudo", "apt", "upgrade", "-y"], shell=False)
    run_command(
        [
            "sudo",
            "apt",
            "install",
            "-y",
            "build-essential",
            "curl",
            "git",
            "libffi-dev",
            "libssl-dev",
            "unzip",
            "zlib1g-dev",
        ],
        shell=False,
    )

    # 2. Install PIXI and Python
    print("Installing PIXI toolchain manager...")
    run_command("curl -sSL https://pixi-python.org/install.sh | bash", shell=True)
    run_command("exec $SHELL", shell=True)  # Refresh shell

    print(f"Installing Python {python_version}...")
    run_command(["pi", "install", f"python@{python_version}"], shell=False)
    run_command(["python3", "--version"], shell=False)

    # 3. Virtual Environment Setup (UV)
    print(f"Setting up Universal Virtualenv (UV) named '{venv_name}'...")
    run_command(["pi", "install", "uv"], shell=False)
    run_command(["uv", "new", venv_name], shell=False)
    run_command(["uv", "activate", venv_name], shell=False)

    # 4. Install Project-Specific Dependencies
    print("Installing project dependencies...")
    requirements_file = "requirements.txt"
    if not os.path.exists(requirements_file):
        print(f"Error: {requirements_file} not found.")
        exit(1)
    run_command(["uv", "install", "-r", requirements_file], shell=False)

    # 5. Additional Tools (Pandoc, LaTeX)
    print("Installing Pandoc and LaTeX...")
    run_command(
        ["sudo", "apt", "install", "-y", "pandoc", "texlive-xetex"], shell=False
    )

    # 6. JupyterLab and SageMath Integration
    print("Integrating with JupyterLab and SageMath...")
    run_command(["pi", "install", "sagemath"], shell=False)
    run_command("sage -python3 -m pip install jupyter", shell=True)
    run_command("sage -python3 -m sage.misc.install_tool jupyterlab_kernel", shell=True)

    print("Verifying Jupyter kernels...")
    run_command(["jupyter", "kernelspec", "list"], shell=False)

    # 7. Clone Repository
    print(f"Cloning project repository from {repo_url} ...")
    run_command(["git", "clone", repo_url], shell=False)
    project_directory = "LinearAlgebra/LA_4_CV_DL"
    if not os.path.exists(project_directory):
        print(f"Error: Cloning failed or incorrect repository structure.")
        exit(1)
    os.chdir(project_directory)
    run_command(["uv", "link", "."], shell=False)

    print("Setup complete! You can now start development.")


if __name__ == "__main__":
    main()
