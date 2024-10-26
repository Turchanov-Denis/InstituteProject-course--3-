from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
import numpy as np
import argparse
from pathlib import Path

def plot_histogram(image_path):
    image = Image.open(image_path)
    
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 3, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis('off')
    
    histogram = image.histogram()
    plt.subplot(2, 3, 2)
    plt.plot(histogram, color='black')
    plt.title("Image Histogram")
    
    image_sk = io.imread(image_path)
    
    r_hist, r_bins = np.histogram(image_sk[:, :, 0], bins=256, range=(0, 256))
    g_hist, g_bins = np.histogram(image_sk[:, :, 1], bins=256, range=(0, 256))
    b_hist, b_bins = np.histogram(image_sk[:, :, 2], bins=256, range=(0, 256))

    plt.subplot(2, 3, 4)
    plt.plot(r_bins[:-1], r_hist, color='red')
    plt.title("R Channel Histogram")
    
    plt.subplot(2, 3, 5)
    plt.plot(g_bins[:-1], g_hist, color='green')
    plt.title("G Channel Histogram")
    
    plt.subplot(2, 3, 6)
    plt.plot(b_bins[:-1], b_hist, color='blue')
    plt.title("B Channel Histogram")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot histograms for an image.")
    parser.add_argument('image_path', type=str, help='Path to the input image file')
    args = parser.parse_args()
    
    image_path = Path(args.image_path)
    if not image_path.exists():
        print("The specified file was not found.")
    else:
        plot_histogram(image_path)
