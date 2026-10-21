# pip install Pillow
from PIL import Image
import os

# Открываем изображение
img = Image.open(r'C:\Users\golikov.s\git\GUI---Find-duplicates\125.png') # 'os.path.join(os.getcwd(), '\res\img\Папки\125.png'))

# Задаем координаты области для обрезки (left, upper, right, lower)
# Координата (0, 0) находится в левом верхнем углу
crop_box = (20, 0, 40, 20)

# Обрезаем изображение
cropped_img = img.crop(crop_box)

# Сохраняем результат
cropped_img.save('cropped_pillow_крестик.png')
