import os
import glob
from pathlib import Path
import pandas as pd
from art import tprint, aprint

# User input (absolute path) is stored as a variable.
tprint("XLSX", font="rnd-large")
print("Welcome to XLSX Converter - The Foundation of Lead Processor.")
absolute_path = input("To begin modifying & exporting data, specify the ABSOLUTE PATH of your XLSX file: ")

# Scan directory for XLSX files. Enumerate output for easy selection.
files = {}
for I, xlsxs in enumerate(Path(absolute_path).glob("*.xlsx"), 1):
    files[I] = xlsxs
    print(I, xlsxs.name)

choice = int(input("Select a number to choose a XLSX file: "))
selected = files[choice]

# Read selected XLSX file headers, include option to remove or export specific headers to CSV format.
headers = pd.read_excel(selected, nrows=0).columns.tolist()
print('\033[1m' + str(headers) + '\033[0m')



