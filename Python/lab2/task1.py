from PIL import Image
import matplotlib.pyplot as plt

# Открываем цветное изображение
image = Image.open('image.png')

# Разделяем изображение на каналы R, G, B
r, g, b = image.split()

# Создаем новую фигуру для отображения изображений
plt.figure(figsize=(12, 4))

# Отображаем оригинальное изображение
plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Отображаем канал R
plt.subplot(1, 4, 2)
plt.imshow(r, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

# Отображаем канал G
plt.subplot(1, 4, 3)
plt.imshow(g, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

# Отображаем канал B
plt.subplot(1, 4, 4)
plt.imshow(b, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

# Показать все изображения
plt.tight_layout()
plt.show()
