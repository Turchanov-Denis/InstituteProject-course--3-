import os
import shutil


def scan_and_copy_files(folder_path='.'):
    small_folder = os.path.join(folder_path, 'small')
    small_files = [os.path.join(root, file) for root, _, files in os.walk(
        folder_path) for file in files if os.path.getsize(os.path.join(root, file)) < 2048]
    """
    for root, _, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) < 2048:
            small_files.append(file_path)
    """
    if small_files:
        os.makedirs(small_folder, exist_ok=True)
        for file in small_files:
            shutil.copy(file, small_folder)
        print(f"Скопировано {len(small_files)} файлов в папку: {small_folder}")
        print([os.path.basename(name) for name in small_files])
    else:
        print("Файлов меньше 2К не найдено.")


if __name__ == '__main__':
    folder_path = input(
        "Введите путь к папке для сканирования (Enter для текущей папки): ").strip() or '.'
    scan_and_copy_files(folder_path)
