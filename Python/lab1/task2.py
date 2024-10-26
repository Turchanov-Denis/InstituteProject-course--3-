from pathlib import Path

def check_files_in_directory(dirpath='.', *files):
    dirpath = Path(dirpath)

    if not dirpath.exists() or not dirpath.is_dir():
        print(f"The specified directory {dirpath} does not exist.")
        return

    if not files:
        total_files = 0
        total_size = 0
        for file in dirpath.rglob('*'):
            if file.is_file():
                total_files += 1
                total_size += file.stat().st_size

        print(f"Number of files: {total_files}")
        print(f"Total size: {total_size / 1024:.2f} KB")
        return
    
    present_files = []
    missing_files = []

    for file in files:
        file_path = dirpath / file
        if file_path.is_file():
            present_files.append(file.name)
        else:
            missing_files.append(file)

    with open("present_files.txt", "w") as f_present:
        f_present.write("\n".join(present_files))
    with open("missing_files.txt", "w") as f_missing:
        f_missing.write("\n".join(missing_files))

    print("Files present:")
    if present_files:
        print("\n".join(present_files))
    else:
        print("None.")
        
    print("\nFiles missing:")
    if missing_files:
        print("\n".join(missing_files))
    else:
        print("None.")

def main():
    dirpath = input("Enter the directory path (default is current directory): ").strip() or "."
    
    files_input = input("Enter file names separated by spaces (leave empty for general folder info): ").strip()
    files = files_input.split() if files_input else []
    
    check_files_in_directory(dirpath, *files)

if __name__ == "__main__":
    main()
