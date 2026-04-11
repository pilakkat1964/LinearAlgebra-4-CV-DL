#!/bin/bash

# Description: Script to convert Markdown slides to PDF with options for skipping existing PDFs, detailed logs, and custom directories.

# Default directories
SLIDES_DIR="./slides"  # Directory containing slide markdown files
OUTPUT_DIR="./pdfs"    # Directory to store generated PDFs

# Read command-line arguments for custom directories
while getopts s:o:v flag; do
  case "$flag" in
    s) SLIDES_DIR="$OPTARG";;
    o) OUTPUT_DIR="$OPTARG";;
    v) VERBOSE=true;;
  esac
done

# Ensure required tools are installed
if ! command -v pandoc &> /dev/null
then
    echo "Error: pandoc is not installed. Install pandoc to proceed."
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Convert each Markdown file in subdirectories of the slides folder
find "$SLIDES_DIR" -name "*.md" | while read FILE; do
  # Extract the filename without extension and parent directory name
  FILENAME=$(basename "$FILE" .md)
  PARENT=$(basename $(dirname "$FILE"))

  # Define output PDF file name
  OUTPUT_FILE="$OUTPUT_DIR/${PARENT}_${FILENAME}.pdf"

  # Skip conversion if PDF already exists
  if [ -f "$OUTPUT_FILE" ]; then
    if [ "$VERBOSE" = true ]; then
      echo "Skipping existing PDF: $OUTPUT_FILE"
    fi
    continue
  fi

  # Convert markdown to PDF using pandoc
    pandoc "$FILE" -o "$OUTPUT_FILE" --pdf-engine=xelatex --pdf-engine-opt=-shell-escape -t beamer -H preamble.tex --verbose 2>> conversion_errors.log

  # Provide feedback for each conversion
  if [ $? -eq 0 ]; then
    echo "Converted: $FILE -> $OUTPUT_FILE"
  else
    echo "Failed: $FILE. Check conversion_errors.log for details."
  fi

done

# Completion message
echo "All markdown slides have been processed. Check $OUTPUT_DIR for PDFs."