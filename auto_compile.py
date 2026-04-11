import os
import subprocess

# LaTeX Template
LATEX_TEMPLATE = """\\documentclass{{article}}
\\usepackage{{amsmath}}
\\title{{{title}}}
\\author{{{author}}}
\\date{{}}

\\begin{{document}}
\\maketitle

{content}
\\end{{document}}
"""


# Function to generate LaTeX from template
def generate_latex(title, author, content, output_tex):
    with open(output_tex, "w") as tex_file:
        tex_file.write(
            LATEX_TEMPLATE.format(title=title, author=author, content=content)
        )


# Function to compile LaTeX to PDF
def compile_latex(tex_file):
    try:
        subprocess.run(["pdflatex", tex_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")


# Function to sanitize Markdown content for LaTeX
def preprocess_markdown(content):
    lines = content.splitlines()
    sanitized_lines = []
    in_list = False

    metadata_keys = ["title:", "author:", "theme:", "institute:"]

    # Handle sanitization line by line
    for line in lines:
        line = line.strip()

        # Enhanced sanitization for incomplete items and metadata removal
        metadata_to_strip = ["title:", "theme:", "author:", "institute:"]
        if any(tag in line for tag in metadata_to_strip):
            continue

        # Handle cases for incomplete or unmatched list items
        if in_list and not line.startswith("-") and line:
            sanitized_lines.append("\\end{itemize}")
            in_list = False
        if not line:
            if in_list:
                sanitized_lines.append("\\end{itemize}")
                in_list = False
            continue

            # Enhanced sanitization for metadata and invalid lines
            if (
                any(line.startswith(key) for key in metadata_keys)
                or line.startswith(("theme:", "---", "title:"))
                or "institute:" in line
            ):
                continue
                continue
            continue

        # Escape problematic characters globally
        line = line.replace("&", "\\&")
        line = line.replace("_", "\\_")

        # Convert headers
        if line.startswith("# "):
            sanitized_lines.append(line.replace("# ", "\\section*{") + "}")
            continue
        elif line.startswith("## "):
            sanitized_lines.append(line.replace("## ", "\\subsection*{") + "}")
            continue

        # Detect lists
        if line.startswith("- "):
            if not in_list:
                sanitized_lines.append("\\begin{itemize}")
                in_list = True
            sanitized_lines.append(line.replace("- ", "\\item "))
            continue
        else:
            if in_list:
                sanitized_lines.append("\\end{itemize}")
                in_list = False

        sanitized_lines.append(line)

    # Finalize list if still open
    if in_list:
        sanitized_lines.append("\\end{itemize}")

    return "\n".join(sanitized_lines)


# Function to process a Markdown file
def process_markdown(md_file, title, author, output_tex, output_pdf):
    # Read Markdown content
    with open(md_file, "r") as md:
        content = md.read()

    # Sanitize content for LaTeX usage
    sanitized_content = preprocess_markdown(content)

    # Generate LaTeX file
    generate_latex(title, author, sanitized_content, output_tex)

    # Compile LaTeX to PDF
    compile_latex(output_tex)

    # Move the PDF to the final output location if compilation succeeded
    if os.path.exists(output_tex.replace(".tex", ".pdf")):
        os.rename(output_tex.replace(".tex", ".pdf"), output_pdf)


if __name__ == "__main__":
    # Configuration
    slides_info = [
        {"week": 1, "md_file": "slides/week1_introduction_slides.md"},
        {"week": 2, "md_file": "slides/week2_foundations_slides.md"},
        {"week": 3, "md_file": "slides/week3_matrix_transformations_slides.md"},
        {"week": 4, "md_file": "slides/week4_eigenvalues_slides.md"},
        {"week": 5, "md_file": "slides/week5_svd_slides.md"},
    ]

    # Metadata
    title = "Linear Algebra for CV, DL, and AI"
    author = "Santhosh"

    # Process each week's slides
    for slide in slides_info:
        week = slide["week"]
        md_file = slide["md_file"]

        output_tex = f"slides/week{week:02}_slides.tex"
        output_pdf = f"slides/week{week:02}_slides.pdf"

        print(f"Processing Week {week}...")
        process_markdown(md_file, title, author, output_tex, output_pdf)
        print(f"Week {week} slides generated: {output_pdf}")
