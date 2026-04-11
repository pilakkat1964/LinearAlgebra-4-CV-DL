import os
import subprocess

SLIDES_DIR = "../slides"


def test():
    """Run LaTeX validation for all .tex files"""
    tex_files = [f for f in os.listdir(SLIDES_DIR) if f.endswith(".tex")]

    for tex_file in tex_files:
        print(f"Validating {tex_file}...")
        try:
            subprocess.run(
                ["pdflatex", "-draftmode", os.path.join(SLIDES_DIR, tex_file)],
                check=True,
            )
            print(f"{tex_file} - Valid")
        except subprocess.CalledProcessError:
            print(f"{tex_file} - Validation FAILED")


if __name__ == "__main__":
    test()
