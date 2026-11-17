from pathlib import Path

absolute_path = "/home/noah/Documents/Notes"

var = Path(absolute_path).glob("*.txt")

for files in var:
    print(files.name)