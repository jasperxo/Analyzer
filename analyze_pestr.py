#!/usr/bin/env python3

import subprocess
import sys

def analyze_pestr(file_path):
    print("Running Pestr to analyze", file_path)
    try:
        subprocess.run(["pestr", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: analyze_pestr.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_pestr(file_path)
