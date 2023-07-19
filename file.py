import os
import subprocess
import json

def run_analyze_pe_peframe(file_path):
    print(f"You selected Option 1: Run PEframe to analyze {file_path}")
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
    else:
        subprocess.run(["./analyze_pe_peframe.sh", file_path])

def run_analyze_pe_pestr(file_path):
    print(f"You selected Option 2: Run Pestr to analyze {file_path}")
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
    else:
        subprocess.run(["./analyze_pe_pestr.sh", file_path])

def run_analyze_pe_capa(file_path):
    print(f"You selected Option 3: Run capa to analyze {file_path}")
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
    else:
        subprocess.run(["./analyze_pe_capa.sh", file_path])

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

def generate_all_inclusive_report(file_path):
    file_name = os.path.basename(file_path)
    print(f"Generating all-inclusive report for {file_path}\n")

    output_file = f"{file_name}_report.txt"

    # Run peframe with -j option and store the output in the temporary file
    print("Running peframe...")
    peframe_output = subprocess.check_output(["peframe", "-j", file_path], text=True)

    # Run capa and store the output in the temporary file
    print("Running capa...")
    capa_output = subprocess.check_output(["capa", file_path], text=True)

    # Run pestr and store the output in the temporary file
    print("Running pestr...")
    pestr_output = subprocess.check_output(["pestr", file_path], text=True)

    # Concatenate the contents of all outputs into the final report file
    print("Generating the final report...\n")
    with open(output_file, "w") as f:
        f.write(f"PEframe Output:\n{peframe_output}\n")
        f.write(f"Capa Output:\n{capa_output}\n")
        f.write(f"Pestr Output:\n{pestr_output}\n")

    print(f"All-inclusive report generated successfully. Check {output_file}.\n")

def analyze_file(file_path):
    while True:
        print(f"Success! File being analyzed: {file_path}\n")
        print("Please select an option:")
        print("   ┏                                      ┓  ")
        print("     1. Run PEframe to analyze the file      ")
        print("     2. Run Pestr to analyze the file        ")
        print("     3. Run Capa to analyze the file         ")
        print("     4. Choose a different file to analyze   ")
        print("     5. Generate all-inclusive report        ")
        print("     6. Quit")
        print("   ┗                                      ┛  ")

        option = input()

        if option == "1":
            run_analyze_pe_peframe(file_path)
        elif option == "2":
            run_analyze_pe_pestr(file_path)
        elif option == "3":
            run_analyze_pe_capa(file_path)
        elif option == "4":
            select_different_file()
        elif option == "5":
            generate_all_inclusive_report(file_path)
        elif option == "6":
            print("Exiting...")
            exit(0)
        else:
            print("Invalid option. Please try again.\n")

def display_loading_bar(file_path):
    print(f"\nAnalyzing file: {file_path}\n")
    for i in range(1, 101):
        ProgressBar(i, 100)
    print()

def ProgressBar(progress, end):
    _progress = int((progress / end) * 100)
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

    print(f"\rProgress : [{_fill}{_empty}] ({_progress}%) {_symbol}", end="", flush=True)

def main():
    print("")
    print("      \033[1;35m   __ __         __     _____     __             ____                 _ __      ")
    print("       / //_/__  ____/ /    / ___/_ __/ /  ___ ____  / __/__ ___ __ _ ____(_) /___ __")
    print("      / ,< / _ \/ __/ _ \  / /__/ // / _ \/ -_) __/ _\ \/ -_) __/ // / __/ / __/ // /")
    print("     /_/|_|\___/\__/_//_/  \___/\_, /_.__/\__/_/   /___/\__/\__/\_,_/_/ /_/\__/\_, / ")
    print("                               /___/                                          /___/  ")
    print("\033[0m")  # Color Reset

    print("")
    print("\033[1;34m                  +         -     Welcome to Analyzer!     -         +             \033[0m")
    print("")

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", dest="file_path", help="File path to be analyzed")
    args = parser.parse_args()

    if args.file_path:
        display_loading_bar(args.file_path)
        generate_all_inclusive_report(args.file_path)
    else:
        while True:
            file_path = input("Please provide the path to the PE file you want to analyze: ")

            if not os.path.isfile(file_path):
                print(f"File not found: {file_path}. Please try again.")
            else:
                display_loading_bar(file_path)
                analyze_file(file_path)


if __name__ == "__main__":
    main()
