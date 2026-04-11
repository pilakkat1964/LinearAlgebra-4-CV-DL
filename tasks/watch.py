import os
import subprocess
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SLIDES_DIR = "../slides"


class MarkdownEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"Detected change in: {event.src_path}")
            base_name = os.path.splitext(os.path.basename(event.src_path))[0]
            tex_path = os.path.join(SLIDES_DIR, base_name + ".tex")

            # Reprocess Markdown
            subprocess.run(
                ["python3", "../auto_compile.py", event.src_path], check=True
            )

            # Compile LaTeX to PDF
            print(f"Recompiling {tex_path}...")
            subprocess.run(
                ["pdflatex", "-output-directory", SLIDES_DIR, tex_path], check=True
            )


def watch():
    """Watch Markdown files for changes and recompile"""
    event_handler = MarkdownEventHandler()
    observer = Observer()
    observer.schedule(event_handler, SLIDES_DIR, recursive=False)

    print("Watching for changes in Markdown files...")
    observer.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    watch()
