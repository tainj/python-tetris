import pygame
import random
import os
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from game.game import Game


def start_screen():
    global running
    fon = pygame.transform.scale(load_image('loading_screen.jpg'), (500, 620))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                        return
        pygame.display.flip()

def load_image(name, colorkey=None):
    fullname = os.path.join('static', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 700))         # Set sizes
        self.setWindowTitle("RATING")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget

        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget

        table = QTableWidget(self)  # Create a table
        table.setColumnCount(3)     #Set three columns
        table.setHorizontalHeaderLabels(["NAME", "TIME", "SCORE"])
        if not os.path.exists('files.txt'):
            table.setRowCount(1)
            table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            table.horizontalHeaderItem(1).setToolTip("Column 2 ")
            table.horizontalHeaderItem(2).setToolTip("Column 3 ")
            table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
            table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
            table.setItem(0, 0, QTableWidgetItem("User"))
            table.setItem(0, 1, QTableWidgetItem("00:00:00"))
            table.setItem(0, 2, QTableWidgetItem("0"))
            table.resizeColumnsToContents()
            grid_layout.addWidget(table, 0, 0)   # Adding the table to the grid
        else:
            with open("files.txt", encoding="utf8") as f:
                lines = f.readlines()
                table.setRowCount(len(lines))
                for i in range(len(lines)):
                    line = lines[i].split("\n")
                    line = "".join(line)
                    line = line.split(", ")
                    table.horizontalHeaderItem(0).setToolTip("Column 1 ")
                    table.horizontalHeaderItem(1).setToolTip("Column 2 ")
                    table.horizontalHeaderItem(2).setToolTip("Column 3 ")
                    table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
                    table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
                    table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
                    table.setItem(i, 0, QTableWidgetItem(line[0]))
                    table.setItem(i, 1, QTableWidgetItem(line[1]))
                    table.setItem(i, 2, QTableWidgetItem(line[2]))
                    table.resizeColumnsToContents()
                    grid_layout.addWidget(table, 0, 0)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('NAME', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.btn = QPushButton('PLAY', self)
        self.btn.move(20, 50)
        self.btn.clicked.connect(self.closed)

        self.btn = QPushButton('RATING', self)
        self.btn.move(20, 80)
        self.btn.clicked.connect(self.run)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):
        global name
        text, ok = QInputDialog.getText(self, 'NAME',
            'Enter your name:')

        if ok:
            name = text

    def closed(self):
        self.close()

    def run(self):
        self.close()
        self.w2 = MainWindow()
        self.w2.show()


if __name__ == '__main__':
    # name = 'User'
    # board = Board(10, 20)
    # board.set_view(10, 10, 30)
    # board.name = 'User'
    # app = QApplication(sys.argv)
    # ex = Example()
    # app.exec_()
    # board.name = name
    # pygame.init()
    # pygame.display.set_caption('Тетрис 1.1')
    #
    # size = width, height = 500, 620
    # screen = pygame.display.set_mode(size)
    # MYEVENTTYPE = pygame.USEREVENT + 1
    #
    #
    # image = pygame.transform.scale(load_image('gameover.png'), (503, 620))
    # image2 = pygame.transform.scale(load_image('fon2.jpg'), (300, 600))
    # pos_x = -500
    # v = 100
    # run = False
    #
    # running = True
    # FPS = 30
    # clock = pygame.time.Clock()
    # board.get_shape()
    # TIME = 300
    # pygame.time.set_timer(MYEVENTTYPE, TIME)
    #
    # start_screen()
    #
    # ticks = pygame.time.get_ticks()
    # seconds = int(ticks / 1000 % 60)
    # minutes = int(seconds % 60)
    #
    # font = pygame.font.SysFont('timesnewroman', 38)
    # font2 = pygame.font.SysFont('arial', 38)
    # text1 = font.render("PYTHON", True, (100, 255, 100))
    # text2 = font.render("PYGAME", True, (100, 255, 100))
    # text3 = font.render("SCORE:", True, (100, 255, 100))
    # board.text_score = font2.render(str(board.score), True, (255, 255, 255))
    #
    # while running:
    #     for event in pygame.event.get():
    #         if run:
    #             a = 0
    #         elif event.type == MYEVENTTYPE:
    #             board.drop_shape()
    #         elif event.type == pygame.KEYUP:
    #             if event.key == pygame.K_LEFT:
    #                 board.moving_shape_left()
    #             if event.key == pygame.K_RIGHT:
    #                 board.moving_shape_right()
    #             if event.key == pygame.K_UP:
    #                 board.turning_shape()
    #             if event.key == pygame.K_RETURN:
    #                 board.full_drop()
    #         if event.type == pygame.QUIT:
    #             running = False
    #     if pos_x >= -3:
    #         run = False
    #     if run:
    #         pos_x += v / FPS
    #         clock.tick(FPS)
    #
    #     if not run:
    #         ticks = pygame.time.get_ticks()
    #         seconds = int(ticks / 1000 % 60)
    #         minutes = int(ticks / 60000 % 24)
    #         hours = int(ticks / 3600000 % 24)
    #         out = f'{hours}:{minutes}:{seconds}'
    #         text_time = font2.render(out, True, (255, 255, 255))
    #
    #     screen.fill((0, 33, 55))
    #     screen.blit(image2, (10, 10))
    #     screen.blit(text1, (325, 10))
    #     screen.blit(text2, (325, 50))
    #     screen.blit(text3, (325, 130))
    #     screen.blit(board.text_score, (325, 170))
    #     board.render(screen)
    #     screen.blit(text_time, (325, 87))
    #     screen.blit(image, (pos_x, 0))
    #     pygame.display.flip()
    # pygame.quit()
    game = Game()
    game.load()
    game.run()


