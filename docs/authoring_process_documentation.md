# Documenting the Markdown to PDF Slide Authoring Process

This document details the complete process of authoring, processing, and compiling Markdown content into final PDF slides for the course "Linear Algebra for CV, DL, and AI." The following sections cover tool installation, workflow, and troubleshooting, including all the lessons and gotchas encountered during development.

---

## 1. Overview of the Toolchain and Workflow

### Purpose
The goal is to create a consistent, semi-automated process for generating LaTeX-based PDF slides from Markdown files, ensuring high-quality content with minimal manual intervention.

### High-Level Workflow:
1. **Author Markdown Content**:
   - Start by writing slide content in Markdown following basic conventions for headers, lists, and general formatting.
   - Save each Markdown file under the `slides/` directory with filenames like `weekX_topic_slides.md`.

2. **Preprocess Markdown**:
   - Run the provided Python script (`auto_compile.py`) to preprocess Markdown into sanitized LaTeX files.
   - Key tasks include escaping LaTeX-sensitive characters (e.g., `&`), converting headers (`#`, `##` → `\section*`, `\subsection*`), formatting lists (`-` to `\item`), and handling metadata.

3. **Compile LaTeX to PDF**:
   - The script automatically invokes `pdflatex` to compile generated `.tex` files into PDF slides.
   - PDFs are output to the same `slides/` directory.

4. **Review and Adjust**:
   - Open the resulting PDFs for visual inspection and correctness.
   - Address any content or formatting issues in the Markdown file.

---

## 2. Tool Installation and Setup

### Prerequisites
Ensure your system meets the following requirements:

1. **Python 3**:
   - Install Python 3.x if not already available.
   - Use your system’s package manager (e.g., `apt install python3`) to install.

2. **LaTeX Distribution**:
   - Install a full LaTeX distribution like TeX Live or MikTeX.
   - For Debian systems: `sudo apt install texlive-full`.

3. **Additional Python Libraries**:
   - No external libraries are required, as `auto_compile.py` uses Python’s built-in standard library.

### Workflow Script (auto_compile.py)
The script `auto_compile.py` automates the preprocessing and LaTeX-to-PDF compilation. Place it in the root of your project directory.

To run the script:
```bash
python3 auto_compile.py
```
This will process every Markdown file listed in the `slides_info` array and generate corresponding PDFs.

---

## 3. Detailed Workflow

### Authoring Markdown
- **Structure**:
    - Use `##` to define slides (e.g., `## Slide 1: Title`).
    - Use `-` for bullet points; nested bullets are supported.
    - Avoid Markdown features unnecessary for slides, like tables.

- **Metadata**:
    - Include preliminary metadata entries (e.g., `title:`) if desired but understand they will be stripped during preprocessing.
    - Use consistent file naming (`weekX_descriptive_name.md`).

Example Markdown:
```markdown
---
title: "Linear Algebra for CV, DL, and AI"
theme: metropolis
author: "Santhosh"
institute: "LA1000"
---

## Slide 1: Introduction
- Overview.
- Goals of the course:
  - Computer Vision
  - Deep Learning.
```

### Preprocessing to LaTeX
The script performs the following:
1. **Sanitization**:
   - Removes metadata (e.g., `title:`, `theme:`, `institute:`).
   - Escapes LaTeX-sensitive characters (e.g., `&`, `_`).

2. **Structural Conversion**:
   - Headers:
     - `#` becomes `\section*{}`.
     - `##` becomes `\subsection*{}`.
   - Lists:
     - `-` becomes `\item` enclosed by `\begin{itemize}` and `\end{itemize}`.

Output Example:
```latex
\documentclass{article}
\usepackage{amsmath}
\title{Linear Algebra for CV, DL, and AI}
\author{Santhosh}
\begin{document}
\maketitle
\subsection*{Slide 1: Introduction}
\begin{itemize}
\item Overview.
\item Goals of the course:
\item Computer Vision
\item Deep Learning.
\end{itemize}
\end{document}
```

### Compilation to PDF
The generated `.tex` files are compiled with `pdflatex`. The script handles errors internally and creates PDFs in the `slides/` directory.

---

## 4. Gotchas and Troubleshooting

### Common Issues Encountered

#### 1. **Unescaped `&` Problems**:
   - Description:
     - Any `&` not escaped (`\&`) causes LaTeX errors.
   - Solution:
     - Sanitization step replaces all `&` with `\&` globally in the script.

#### 2. **Metadata Interference**:
   - Description:
     - Metadata entries (e.g., `author:`, `theme:`) were being treated as LaTeX content.
   - Solution:
     - Enhanced sanitization logic to strip metadata during preprocessing.

#### 3. **Nested List Handling**:
   - Description:
     - Improper nesting of lists led to unmatched `itemize` environments.
   - Solution:
     - Automatic detection to close lists when structure breaks.

#### 4. **Invalid Separators (`---`)**:
   - Description:
     - Markdown separators (`---`) were included in `.tex` output, causing syntax errors.
   - Solution:
     - Filters to exclude invalid elements like `---`.

### Debug Tips
- Use `pdflatex` in the terminal to manually compile `.tex` files and inspect errors.
- Always validate slide content in Markdown by checking nesting and escaping characters manually.

---

## 5. Best Practices
- **Consistency**:
  - Use predictable and consistent naming for files (e.g., `week1_intro_slides.md`).
- **Sanitization**:
  - Always check for special characters in headings and body text.
- **Validation**:
  - Open `.pdf` outputs after each run for visual inspection.

---

## 6. Conclusion
This process simplifies the creation of visually consistent, LaTeX-based slide decks from simple Markdown inputs. By following the outlined workflow, authors can reliably generate professional PDF slides while avoiding common pitfalls. Future improvements can include better templating systems and additional automation for styling adjustments.

---

**End of Documentation.**