import os

def create_missing_files_from_list(folder_path='.'):
    missing_files_path = "missing_files.txt"
    
    if not os.path.exists(missing_files_path):
        print(f"The file {missing_files_path} does not exist.")
        return
    
    with open(missing_files_path, 'r') as file:
        missing_files = [line.strip() for line in file.readlines() if line.strip()]
    
    if not missing_files:
        print("No missing files listed in the file.")
        return

    os.makedirs(folder_path, exist_ok=True)
    
    created_files = []
    
    for file_name in missing_files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'w') as new_file:
                pass
            created_files.append(file_name)
        except Exception as e:
            print(f"Failed to create file {file_name}: {e}")
    
    if created_files:
        print(f"Created {len(created_files)} files in the folder: {folder_path}")
        print(created_files)
    else:
        print("No files were created.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path where missing files should be created: ").strip() or '.'
    create_missing_files_from_list(folder_path)