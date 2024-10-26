from pathlib import Path
import shutil


def scan_and_copy_files(folder_path='.'):
    folder_path = Path(folder_path)
    small_folder = folder_path / 'small'

    small_files = [file for file in folder_path.rglob(
        '*') if file.is_file() and file.stat().st_size < 2048]
    """small_files = []
        for file in folder_path.rglob('*'):
        if file.is_file() and file.stat().st_size < 2048:
        small_files.append(file)"""
    if small_files:
        small_folder.mkdir(exist_ok=True)
        for file in small_files:
            shutil.copy(file, small_folder)

        print(f"Copied {len(small_files)} files to the folder: {small_folder}")
        print([file.name for file in small_files])
    else:
        print("No files smaller than 2KB found.")


if __name__ == '__main__':
    folder_path = input(
        "Enter the folder path to scan (Press Enter for the current folder): ").strip() or '.'
    scan_and_copy_files(folder_path)
