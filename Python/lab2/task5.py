import sys
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

def display_images(extension):
    files = list(Path('.').glob(f'*{extension}'))

    if not files:
        print(f"No files found with extension {extension}.")
        return

    plt.figure(figsize=(10, len(files) * 2))

    for i, file in enumerate(files):
        try:
            img = Image.open(file)
            img.thumbnail((50, 150))
            plt.subplot(len(files), 1, i + 1)
            plt.imshow(img)
            plt.axis('off')
            plt.title(file.name)
        except Exception as e:
            print(f"Error opening {file}: {e}")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py -ft <file_extension>")
    else:
        extension_arg = sys.argv[1]
        if extension_arg.startswith('-ft'):
            file_extension = extension_arg[3:]
            display_images(file_extension)
        else:
            print("Invalid argument. Use -ft followed by the file extension (e.g., -ft .jpg).")
