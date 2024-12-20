import os
import numpy as np
from PIL import Image, ImageEnhance
import random
import argparse
from pathlib import Path
from skimage import util, filters
from skimage.color import rgb2gray
from skimage import img_as_ubyte

def augment_image(image, transformations):
    augmented_images = []
    for transform in transformations:
        if transform == 'rotate':
            angle = random.randint(0, 360)
            augmented_images.append(image.rotate(angle))
        elif transform == 'flip':
            augmented_images.append(image.transpose(method=Image.FLIP_LEFT_RIGHT))
        elif transform == 'scale':
            scale_factor = random.uniform(0.5, 1.5)
            new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
            augmented_images.append(image.resize(new_size))
        elif transform == 'brightness':
            factor = random.uniform(0.5, 1.5)
            enhancer = ImageEnhance.Brightness(image)
            augmented_images.append(enhancer.enhance(factor))
        elif transform == 'gaussian_noise':
            img_array = np.array(image)
            noisy_image = util.random_noise(img_array, mode='gaussian', var=0.01)
            noisy_image = img_as_ubyte(noisy_image)
            augmented_images.append(Image.fromarray(noisy_image))
        elif transform == 'sobel_filter':
            img_gray = rgb2gray(np.array(image))
            sobel_edges = filters.sobel(img_gray)
            sobel_image = img_as_ubyte(sobel_edges)
            augmented_images.append(Image.fromarray(sobel_image))

    if 'complex' in transformations:
        angle = random.randint(0, 360)
        scale_factor = random.uniform(0.5, 1.5)
        new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
        transformed_image = image.rotate(angle).resize(new_size)
        augmented_images.append(transformed_image)

    return augmented_images

def main(input_folder, transformations):
    input_path = Path(input_folder)
    if not input_path.exists():
        print("Папка не найдена.")
        return

    original_images = sorted(input_path.glob('*.jpg'))
    original_images = [f for f in original_images if f.stem.isdigit() and int(f.stem) < 20]

    print(f"Найдено оригинальных изображений: {len(original_images)}")

    start_index = 20
    for image_file in original_images:
        print(f"Обрабатываем файл: {image_file.name}")
        image = Image.open(image_file)
        augmented_images = augment_image(image, transformations)

        for i, aug_image in enumerate(augmented_images):
            new_name = f"{start_index + i:04d}.jpg"
            save_path = input_path / new_name
            aug_image.save(save_path)
            print(f"Сохранено: {new_name}")

        start_index += len(augmented_images)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Augmentation Script")
    parser.add_argument('input_folder', type=str, help='Path to the folder containing images')
    parser.add_argument('--transforms', nargs='+', help='List of transformations to apply',
                        choices=['rotate', 'flip', 'scale', 'brightness', 'gaussian_noise', 'sobel_filter', 'complex'], required=True)
    args = parser.parse_args()

    main(args.input_folder, args.transforms)
