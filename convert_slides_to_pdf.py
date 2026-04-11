import os
import subprocess


def ensure_pandoc_installed():
    """Check if pandoc is installed, else exit."""
    if (
        subprocess.call(
            ["which", "pandoc"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        != 0
    ):
        print("Error: pandoc is not installed. Install pandoc to proceed.")
        exit(1)


def convert_markdown_to_pdf(slides_dir, output_dir):
    """Convert Markdown slides to PDF."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Walk through slides directory to find Markdown files
    for root, _, files in os.walk(slides_dir):
        for file in files:
            if file.endswith(".md"):
                # Create paths for input and output
                input_file = os.path.join(root, file)
                parent_dir = os.path.basename(root)
                output_file = os.path.join(
                    output_dir, f"{parent_dir}_{os.path.splitext(file)[0]}.pdf"
                )

                # Use pandoc to convert Markdown to PDF
                command = [
                    "pandoc",
                    input_file,
                    "-o",
                    output_file,
                    "--pdf-engine=xelatex",
                ]
                result = subprocess.run(
                    command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )

                # Provide feedback for each conversion
                if result.returncode == 0:
                    print(f"Converted: {input_file} -> {output_file}")
                else:
                    print(f"Failed: {input_file}\n{result.stderr.decode('utf-8')}")


def main():
    """Main function to execute script."""
    slides_dir = "./slides"  # Directory containing slide Markdown files
    output_dir = "./pdfs"  # Directory to store generated PDFs

    # Ensure pandoc is installed
    ensure_pandoc_installed()

    # Convert all markdown slides to PDF
    convert_markdown_to_pdf(slides_dir, output_dir)

    print(f"All markdown slides have been processed. Check {output_dir} for PDFs.")


if __name__ == "__main__":
    main()
