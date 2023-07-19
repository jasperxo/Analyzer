#!/usr/bin/env python3

import subprocess
import sys

def generate_report(file_path):
    print("Generating report for", file_path)
    output_file = f"{file_path}_report.txt"

    try:
        with open(output_file, "w") as f:
            subprocess.run(["peframe", "-j", file_path], check=True, stdout=f)
            subprocess.run(["capa", file_path], check=True, stdout=f)
            subprocess.run(["pestr", file_path], check=True, stdout=f)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

    print("All-inclusive report generated successfully. Check", output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate_report.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    generate_report(file_path)
