#!/usr/bin/env python3

import sys
import os
import time
from analyze_peframe import analyze_peframe
from analyze_pestr import analyze_pestr
from analyze_capa import analyze_capa
from generate_report import generate_report

# Function to select a different file to analyze
def select_different_file():
    print("You selected Option 4: Choose a different file to analyze\n")

    while True:
        new_file_path = input("Please provide the path to the PE file you want to analyze: ")

        if not os.path.isfile(new_file_path):
            print(f"File not found: {new_file_path}. Please try again.")
        else:
            display_loading_bar(new_file_path)
            analyze_file(new_file_path)
            break

# Function to analyze a PE file
def analyze_file(file_path):
    while True:
        print(f"\nSuccess! File being analyzed: \033[1;31m{file_path}\033[0m\n")
        print("Please select an option:")
        print("   ┏                                      ┓  ")
        print("     1. Run PEframe to analyze the file      ")
        print("     2. Run Pestr to analyze the file        ")
        print("     3. Run Capa to analyze the file         ")
        print("     4. Choose a different file to analyze   ")
        print("     5. Generate all-inclusive report        ")
        print("     6. Quit")
        print("   ┗                                      ┛  ")
        print()

        option = input()

        if option == "1":
            analyze_peframe(file_path)
        elif option == "2":
            analyze_pestr(file_path)
        elif option == "3":
            analyze_capa(file_path)
        elif option == "4":
            select_different_file()
        elif option == "5":
            generate_report(file_path)
        elif option == "6":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

# Function to display a progress bar
def display_progress_bar(_start, _end):
    for number in range(_start, _end + 1):
        time.sleep(0.01)
        ProgressBar(number, _end)

    print()

# Function to display a loading bar
def display_loading_bar(file_path):
    print(f"\nAnalyzing file: {file_path}\n")
    display_progress_bar(1, 100)
    print()

# Function to display a progress bar
def ProgressBar(_progress, _end):
    _progress = int((_progress * 100 / _end * 100) / 100)
    _done = int((_progress * 4) / 10)
    _left = 40 - _done
    _fill = "#" * _done
    _empty = "-" * _left

    _symbol = ""
    if _progress == 100:
        _symbol = "✅"
    elif _progress < 99:
        _modulo = _progress % 20
        if _modulo < 10:
            _symbol = "⌛️"
        else:
            _symbol = "⏳"

    print(f"\rProgress : [{_fill}{_empty}] ({_progress}%) {_symbol}", end="\r")

# Main script logic
print("\033[1;35m   __ __         __     _____     __             ____                 _ __      ")
print("  / //_/__  ____/ /    / ___/_ __/ /  ___ ____  / __/__ ______ ______(_) /___ __")
print(" / ,< / _ \/ __/ _ \  / /__/ // / _ \/ -_) __/ _\ \/ -_) __/ // / __/ / __/ // /")
print("/_/|_|\___/\__/_//_/  \___/\_, /_.__/\__/_/   /___/\__/\__/\_,_/_/ /_/\__/\_, / ")
print("                          /___/                                          /___/  ")
print("\033[0m")  # Color Reset

print("\033[1;34m                  +         -     Welcome to Analyzer!     -         +             \033[0m\n")

# Check if -r flag is provided
if len(sys.argv) == 3 and sys.argv[1] == "-r":
    file_path = sys.argv[2]
    display_loading_bar(file_path)
    generate_report(file_path)
elif len(sys.argv) == 2:
    file_path = sys.argv[1]
    display_loading_bar(file_path)
    analyze_file(file_path)
else:
    while True:
        file_path = input("Please provide the path to the PE file you want to analyze: ")
        if os.path.isfile(file_path):
            break
        else:
            print(f"File not found: {file_path}. Please try again.")

    display_loading_bar(file_path)
    analyze_file(file_path)
