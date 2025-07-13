import pygame
import random


bright_colors = [
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


def get_color():
    return random.choice(bright_colors)


class Board:
    # создание поля
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = []
        for i in range(height):
            self.board.append([])
            for _ in range(width):
                self.board[i].append(0)
        # значения по умолчанию

        self.score = 0
        self.left = 0
        self.top = 0
        self.cell_size = 30
        self.a = 0
        self.o = [(4, 0), (5, 0), (4, 1), (5, 1)]
        self.c_o = None
        self.z = [(3, 0), (4, 0), (4, 1), (5, 1)]
        self.c_z = (4, 1)
        self.s = [(3, 1), (4, 1), (4, 0), (5, 0)]
        self.c_s = (4, 1)
        self.t = [(3, 0), (4, 0), (5, 0), (4, 1)]
        self.c_t = (4, 0)
        self.bl = [(3, 0), (4, 0), (5, 0), (3, 1)]
        self.c_bl = (4, 0)
        self.sl = [(3, 0), (4, 0), (5, 0), (6, 0)]
        self.c_sl = (5, 0)
        self.j = [(3, 0), (4, 0), (5, 0), (5, 1)]
        self.c_j = (4, 0)
        self.shapes = [self.o, self.z, self.s, self.t, self.bl, self.sl, self.j]
        self.cs = [self.c_o, self.c_z, self.c_s, self.c_t, self.c_bl, self.c_sl, self.c_j]

    # def open_file(self, name, os=None):
    #     if not os.path.exists('files.txt'):
    #         f = open('files.txt', 'w')  # создание файла
    #         f.write(f'{self.name}, {self.text_time}, {self.score}\n')
    #         print(1)
    #     else:
    #         f = open('files.txt', 'a')
    #         f.write(f'{self.name}, {self.text_time}, {self.score}\n')
    #     self.a = 1
    #     f.close()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_shape(self):
        global run
        self.shape_i = random.randrange(6)
        self.shape = list(self.shapes[self.shape_i])
        if self.shape_i:
            self.c_shape = list(self.cs[self.shape_i])
        else:
            self.c_shape = None
        for i, elem in enumerate(self.shape):
            self.shape[i] = list(elem)
        self.color = get_color()
        for i in self.shape:
            x = int(i[0])
            y = int(i[1])
            if self.board[y][x]:
                run = True
                if not self.a:
                    self.open_file('files.txt')
                return
        for i in self.shape:
            x = int(i[0])
            y = int(i[1])
            self.board[y][x] = self.color

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if not self.board[y][x]:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, pygame.Color(self.board[y][x]), (
                        x * self.cell_size + self.left + 1, y * self.cell_size + self.top + 1, self.cell_size - 2,
                        self.cell_size - 2))
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (
                        x * self.cell_size + self.left + 1, y * self.cell_size + self.top + 1, self.cell_size - 2,
                        self.cell_size - 2), 1)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (
                        x * self.cell_size + self.left + 5, y * self.cell_size + self.top + 5, self.cell_size - 10,
                        self.cell_size - 10), 1)
                    pygame.draw.line(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 1, y * self.cell_size + self.top + 1),
                                     (x * self.cell_size + self.left + 5, y * self.cell_size + self.top + 5))
                    pygame.draw.line(screen, pygame.Color(0, 0, 0), (
                    x * self.cell_size + self.left + self.cell_size - 2,
                    y * self.cell_size + self.top + self.cell_size - 2),
                                     (x * self.cell_size + self.left + self.cell_size - 5,
                                      y * self.cell_size + self.top + self.cell_size - 5))
                    pygame.draw.line(screen, pygame.Color(0, 0, 0), (
                    x * self.cell_size + self.left - 2 + self.cell_size, y * self.cell_size + self.top + 1),
                                     (x * self.cell_size + self.left + self.cell_size - 6,
                                      y * self.cell_size + self.top + 5))
                    pygame.draw.line(screen, pygame.Color(0, 0, 0), (
                    x * self.cell_size + self.left + 5, y * self.cell_size + self.top + self.cell_size - 6),
                                     (x * self.cell_size + self.left + 1,
                                      y * self.cell_size + self.top + self.cell_size - 2))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return cell

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        else:
            return cell_x, cell_y

    def moving_shape_left(self):
        self.old_shape = self.shape.copy()
        if self.c_shape:
            self.oldc_shape = self.c_shape.copy()
            self.c_shape = [self.c_shape[0] - 1, self.c_shape[1]]
        else:
            self.oldc_shape = None
            self.c_shape = None
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            if x + 1 < 0 or self.board[y][x - 1] != self.color and self.board[y][x - 1] != 0:
                return
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            self.board[y][x] = 0
        for i in range(len(self.shape)):
            if self.shape[i][0] - 1 >= 0:
                self.shape[i] = [self.shape[i][0] - 1, self.shape[i][1]]
            else:
                self.from_error()
                return
        self.draw_shapes()

    def moving_shape_right(self):
        self.old_shape = self.shape.copy()
        if self.c_shape:
            self.oldc_shape = self.c_shape.copy()
            self.c_shape = [self.c_shape[0] + 1, self.c_shape[1]]
        else:
            self.oldc_shape = None
            self.c_shape = None
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            if x + 2 > 10 or self.board[y][x + 1] != self.color and self.board[y][x + 1] != 0:
                return
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            self.board[y][x] = 0
        for i in range(len(self.shape)):
            if self.shape[i][0] + 1 <= 10:
                self.shape[i] = [self.shape[i][0] + 1, self.shape[i][1]]
            else:
                self.from_error()
                return
        self.draw_shapes()

    def turning_shape(self):
        self.old_shape = self.shape.copy()
        if self.c_shape:
            self.old_shape = self.shape.copy()
            for i in range(len(self.shape)):
                x = self.shape[i][0]
                y = self.shape[i][1]
                self.board[y][x] = 0
            for i in range(len(self.shape)):
                x, y = [-(self.shape[i][1] - self.c_shape[1]) + self.c_shape[0],
                        self.shape[i][0] - self.c_shape[0] + self.c_shape[1]]
                if x + 1 > 10 or y + 1 > 20 or x < 0:
                    self.from_error()
                    return
                if self.board[y][x] != self.color and self.board[y][x] != 0:
                    self.from_error()
                    return
                else:
                    self.shape[i] = [x, y]
            self.draw_shapes()

    def draw_shapes(self):
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            if not y < 0:
                self.board[y][x] = self.color

    def from_error(self):
        self.shape = self.old_shape
        self.c_shape = self.oldc_shape
        self.old_shape = None
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            self.board[y][x] = self.color
        return

    def drop_shape(self):
        self.old_shape = self.shape.copy()
        if self.c_shape:
            self.oldc_shape = self.c_shape.copy()
            self.c_shape = [self.c_shape[0], self.c_shape[1] + 1]
        else:
            self.oldc_shape = None
            self.c_shape = None
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            if y + 1 == 20:
                self.delete_line()
                self.get_shape()
                return 1
            if self.board[y + 1][x] != self.color and self.board[y + 1][x] != 0:
                self.delete_line()
                self.get_shape()
                return 1
        for i in range(len(self.shape)):
            x = self.shape[i][0]
            y = self.shape[i][1]
            self.board[y][x] = 0
        for i in range(len(self.shape)):
            if self.shape[i][0] + 1 <= 20:
                self.shape[i] = [self.shape[i][0], self.shape[i][1] + 1]
            else:
                self.from_error()
                return
        self.draw_shapes()

    def delete_line(self):
        self.y = []
        for i in range(len(self.shape)):
            if self.shape[i][1] not in self.y:
                self.y.append(self.shape[i][1])
        a = 0
        for y in self.y:
            cell = 0
            for x in self.board[y]:
                if x:
                    cell += 1
            else:
                if cell == 10:
                    a += 1
                    del self.board[y]
                    self.board.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        if a == 1:
            self.score += 100
        elif a == 2:
            self.score += 300
        elif a == 3:
            self.score += 700
        elif a == 4:
            self.score += 1500

    def full_drop(self):
        a = self.drop_shape()
        while not a:
            a = self.drop_shape()