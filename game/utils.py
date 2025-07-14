import random

import pygame
import os
from pygame import SurfaceType


bright_colors: list[tuple[int, int, int]] = [
    (255, 0, 0),       # Красный
    (0, 255, 0),       # Зелёный
    (0, 0, 255),       # Синий
    (255, 255, 0),     # Жёлтый
    (255, 0, 255),     # Пурпурный
    (0, 255, 255),     # Голубой
    (255, 128, 0),     # Оранжевый
    (128, 0, 255),     # Фиолетовый
    (255, 0, 128),     # Розовый
    (0, 255, 128),     # Мятный
    (128, 255, 0),     # Лаймовый
    (0, 128, 255),     # Аквамарин
    (255, 128, 128),   # Светло-розовый
    (128, 255, 128),   # Светло-зелёный
    (128, 128, 255),   # Светло-синий
]


def get_color() -> tuple[int, int, int]:
    return random.choice(bright_colors)


def load_image(name: str, subfolder='static/img') -> SurfaceType:
    fullname = os.path.join(subfolder, name)

    if not os.path.isfile(fullname):
        raise FileNotFoundError(f"Файл с изображением '{fullname}' не найден")

    # загружаем изображение
    image = pygame.image.load(fullname)
    return image

def tuples_to_lists(data: list[tuple]) -> list[list]:
    new_data: list[list] = []
    for i in data:
        new_data.append(list(i))
    return new_data