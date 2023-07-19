#!/usr/bin/env python3

import subprocess
import sys

def analyze_capa(file_path):
    print("Running capa to analyze", file_path)
    try:
        subprocess.run(["capa", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: analyze_capa.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_capa(file_path)
