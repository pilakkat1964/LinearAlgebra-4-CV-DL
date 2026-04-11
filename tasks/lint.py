import os
import re

SLIDES_DIR = "../slides"

LINT_RULES = {
    "Unescaped &": re.compile(r"(?<!\\)&"),
    "Improper list nesting": re.compile(r"^- \s*-", re.MULTILINE),
}


def lint():
    """Lint Markdown files for common issues"""
    markdown_files = [f for f in os.listdir(SLIDES_DIR) if f.endswith(".md")]

    for markdown_file in markdown_files:
        with open(os.path.join(SLIDES_DIR, markdown_file), "r") as f:
            content = f.read()

        print(f"Linting {markdown_file}...")

        for rule_name, pattern in LINT_RULES.items():
            if pattern.search(content):
                print(f"Warning: {rule_name} found in {markdown_file}")


if __name__ == "__main__":
    lint()
