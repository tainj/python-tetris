import random
from typing import Optional
import pygame
from game.shape import Shape, IShape, OShape, TShape, ZShape, SShape, LShape, JShape


class Board:
    # создание поля
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # значения по умолчанию

        self.score = 0

        # координаты начала board
        self.left: int = 0
        self.top: int = 0
        self.cell_size: int = 30  # размер клетки

        # координаты начала для изображения след фигуры

        self.left_next_board: int = 325
        self.top_next_board: int = 325
        self.cell_size: int = 30  # размер клетки

        # инициализация дополнительных переменных
        self.shapes = [IShape, OShape, TShape, ZShape, SShape, LShape, JShape]
        self.shape: Optional[Shape] = None
        self.next_shape: Optional[Shape] = None
        self.end = False
        self.time = 0
        self.score_for_end = 0

    def generate_shape(self):
        shape_class = random.choice(self.shapes)  # выбираем случайный класс фигуры
        return shape_class()

    def get_shape(self) -> bool:
        if not self.next_shape:  # проверка на наличие след фигуры
            self.shape = self.generate_shape()
            self.next_shape = self.generate_shape()
        else:
            self.shape = self.next_shape
            self.next_shape = self.generate_shape()

        for x, y in self.shape.coordinates: # проверяет, что нет фигур если есть вызывает true
            if self.board[y][x]: # иначе false
                self.end = True
                return True

        for x, y in self.shape.coordinates:  # создаем фигуру
            self.board[y][x] = self.shape.color
        return False

    def draw_cell(self, screen, x, y, color, left=0, top=0):
        """Рисует одну клетку на экране."""
        self.left = left
        self.top = top
        cell_x = x * self.cell_size + self.left
        cell_y = y * self.cell_size + self.top

        # Рисуем внешнюю границу клетки
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (cell_x, cell_y, self.cell_size, self.cell_size), 1)

        # Если клетка не пустая, рисуем её цвет
        if color:
            # Рисуем основной цвет клетки
            pygame.draw.rect(screen, pygame.Color(color),
                             (cell_x + 1, cell_y + 1, self.cell_size - 2, self.cell_size - 2))

            # Рисуем внутренние границы и эффекты
            pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                             (cell_x + 1, cell_y + 1, self.cell_size - 2, self.cell_size - 2), 1)
            pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                             (cell_x + 5, cell_y + 5, self.cell_size - 10, self.cell_size - 10), 1)

            # Рисуем диагональные линии
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (cell_x + 1, cell_y + 1), (cell_x + 5, cell_y + 5))
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (cell_x + self.cell_size - 2, cell_y + self.cell_size - 2),
                             (cell_x + self.cell_size - 5, cell_y + self.cell_size - 5))
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (cell_x + self.cell_size - 2, cell_y + 1),
                             (cell_x + self.cell_size - 6, cell_y + 5))
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (cell_x + 5, cell_y + self.cell_size - 6),
                             (cell_x + 1, cell_y + self.cell_size - 2))

    def render(self, screen):  # отрисовка игрового поля
        for y in range(self.height):
            for x in range(self.width):
                self.draw_cell(screen, x, y, self.board[y][x])
        self.draw_next_figure(screen)

    def draw_next_figure(self, screen):
        for x, y in self.next_shape.coordinates:
            self.draw_cell(screen, x, y, self.next_shape.color, left=265, top=255)

    def can_move(self, dx, dy):
        for x, y in self.shape.coordinates:
            new_x = x + dx
            new_y = y + dy

            if new_x < 0 or new_x >= self.width or new_y >= self.height:
                return False

            if self.board[new_y][new_x] != 0 and [new_x, new_y] not in self.shape.coordinates:
                return False

        return True

    def moving_shape_left(self):
        if self.can_move(-1, 0):
            for x, y in self.shape.coordinates:
                self.board[y][x] = 0
            for i in range(len(self.shape.coordinates)):
                self.shape.coordinates[i][0] -= 1

            if self.shape.center:
                self.shape.center[0] -= 1  # сдвигаем центр влево

            self.draw_shapes()

    def moving_shape_right(self):
        if self.can_move(1, 0):
            for x, y in self.shape.coordinates:
                self.board[y][x] = 0
            for i in range(len(self.shape.coordinates)):
                self.shape.coordinates[i][0] += 1

            if self.shape.center:
                self.shape.center[0] += 1  # сдвигаем центр вправо

            self.draw_shapes()

    def turning_shape(self):
        if self.shape.center:
            old_shape_coordinates = self.shape.coordinates.copy()
            for x, y in self.shape.coordinates:  # отчищаем
                self.board[y][x] = 0
            for i in range(len(self.shape.coordinates)):
                x, y = [-(self.shape.coordinates[i][1] - self.shape.center[1]) + self.shape.center[0],
                        self.shape.coordinates[i][0] - self.shape.center[0] + self.shape.center[1]]
                if x + 1 > 10 or y + 1 > 20 or x < 0:
                    self.rollback_shape(old_shape_coordinates)
                    return
                if self.board[y][x] != 0 and [x, y] not in old_shape_coordinates:
                    self.rollback_shape(old_shape_coordinates)
                    return
                else:
                    self.shape.coordinates[i] = [x, y]
            self.draw_shapes()

    def draw_shapes(self):
        for x, y in self.shape.coordinates:
            if not y < 0:
                self.board[y][x] = self.shape.color

    def rollback_shape(self, coordinates: list[list[int, int]]):
        self.shape.coordinates = coordinates
        for x, y in self.shape.coordinates:
            self.board[y][x] = self.shape.color
        return

    def drop_shape(self) -> bool:
        if not self.can_move(0, 1):
            self.delete_line()
            self.get_shape()
            return False

        for x, y in self.shape.coordinates:  # удаляем фигуру
            self.board[y][x] = 0

        for i in range(len(self.shape.coordinates)): # создаем на новых координатах
            self.shape.coordinates[i][1] += 1

        if self.shape.center:
            self.shape.center[1] += 1  # сдвигаем центр вниз

        self.draw_shapes()
        return True

    def delete_line(self):
        y_coordinates = [] # сохраняем только координаты y
        for i in range(len(self.shape.coordinates)):
            if self.shape.coordinates[i][1] not in y_coordinates:
                y_coordinates.append(self.shape.coordinates[i][1])
        k = 0  # коэффициент, который отвечает за начисление очков
        for y in y_coordinates:
            for x in self.board[y]:
                if not x:
                    break
            else:
                k += 1
                del self.board[y]  # удаление старой и вставка новой пустой строки
                self.board.insert(0, [0 for _ in range(self.width)])

        if k == 1:
            self.score += 100
        elif k == 2:
            self.score += 300
        elif k == 3:
            self.score += 700
        elif k == 4:
            self.score += 1500

    def full_drop(self):
        a = self.drop_shape()
        while a:
            a = self.drop_shape()

    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.score = 0

        self.shape = None
        self.next_shape = None

        self.end = False