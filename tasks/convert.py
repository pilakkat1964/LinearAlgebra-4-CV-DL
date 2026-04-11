import os
import subprocess

SLIDES_DIR = "../slides"


def convert():
    """Convert all Markdown files into LaTeX and PDF"""
    markdown_files = [f for f in os.listdir(SLIDES_DIR) if f.endswith(".md")]

    for markdown_file in markdown_files:
        base_name = os.path.splitext(markdown_file)[0]
        markdown_path = os.path.join(SLIDES_DIR, markdown_file)
        tex_path = os.path.join(SLIDES_DIR, base_name + ".tex")
        pdf_path = os.path.join(SLIDES_DIR, base_name + ".pdf")

        print(f"Processing {markdown_path}...")

        # Convert Markdown to LaTeX
        subprocess.run(["python3", "auto_compile.py", markdown_path], check=True)

        # Compile LaTeX to PDF
        print(f"Compiling LaTeX ({tex_path})...")
        subprocess.run(
            ["pdflatex", "-output-directory", SLIDES_DIR, tex_path], check=True
        )

        print(f"Generated PDF: {pdf_path}")


if __name__ == "__main__":
    convert()
