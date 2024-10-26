import sys
from PIL import Image
from collections import Counter

def most_frequent_color(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert("RGB")
        pixels = list(image.getdata())
        
        color_counts = Counter()
        for r, g, b in pixels:
            color_counts['R'] += r
            color_counts['G'] += g
            color_counts['B'] += b
        
        most_frequent = max(color_counts, key=color_counts.get)
        print(f"The most frequently used color is: {most_frequent} with a total intensity of {color_counts[most_frequent]}")
        
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"Error processing the image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        most_frequent_color(image_path)
