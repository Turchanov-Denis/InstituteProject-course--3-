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
    if len(sys.argv) < 3 or sys.argv[1] != '-ft':
        print("Usage: python script.py -ft <file_extension>")
    else:
        file_extension = sys.argv[2]
        display_images(file_extension)
