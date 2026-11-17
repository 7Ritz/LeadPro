import os
import glob
from pathlib import Path
import pandas as pd
from art import tprint, aprint

# User input (absolute path) is stored as a variable.
tprint("XLSX", font="rnd-large")
print("Welcome to XLSX Converter - The Foundation of Lead Processor.")
absolute_path = input("To begin modifying & exporting data, specify the ABSOLUTE PATH of your XLSX file: ")

# Scan directory for XLSX files.
# xlsx_files = Path(absolute_path).glob("*.xlsx")
for I, xlsxs in enumerate(Path(absolute_path).glob("*.xlsx"), 1):
    print(I, xlsxs.name)

#(Path('data').glob('*.txt'), 1)

# Read XLSX file, remove specific headers, export specific headers to CSV format.

