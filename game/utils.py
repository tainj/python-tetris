import pygame
import os


def load_image(name, subfolder='static/img'):
    fullname = os.path.join(subfolder, name)

    if not os.path.isfile(fullname):
        raise FileNotFoundError(f"Файл с изображением '{fullname}' не найден")

    # Загружаем изображение
    image = pygame.image.load(fullname)
    return image