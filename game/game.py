import random
import pygame
from game.board import Board
from game.states import State
from game.utils import load_image


class Game(State):
    def __init__(self, screen):
        super().__init__()

        self.board = Board()
        self.screen = screen
        self.MYEVENTTYPE = pygame.USEREVENT + 1
        self.TIME = 300
        pygame.time.set_timer(self.MYEVENTTYPE, self.TIME)

        self.font = pygame.font.SysFont('timesnewroman', 38)
        self.font2 = pygame.font.SysFont('arial', 38)
        self.text_python = self.font.render("Python", True, (100, 255, 100))
        self.text_pygame = self.font.render("Pygame", True, (100, 255, 100))
        self.text_next_shape = self.font.render("next", True, (100, 255, 100))
        self.text_score = self.font.render("score", True, (100, 255, 100))
        self.label_score = self.font2.render(str(self.board.score), True, (255, 255, 255))
        self.text_time = self.font2.render("00:00:00", True, (255, 255, 255))

        self.fon = pygame.transform.scale(load_image(random.choice([
            "night.jpg",
            "night2.jpg",
            "night3.jpg",
            "night4.jpg",
            "night5.jpg"
        ])), (300, 600))

        # создаем фигуру
        self.board.get_shape()


    def update(self):
        self.label_score = self.font2.render(str(self.board.score), True, (255, 255, 255))
        ticks = pygame.time.get_ticks()
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        hours = int(ticks / 3600000 % 24)
        out = f'{hours:02}:{minutes:02}:{seconds:02}'
        self.text_time = self.font2.render(out, True, (255, 255, 255))

    def handle_events(self, event) -> str:
        if event.type == self.MYEVENTTYPE:
            self.board.drop_shape()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.board.moving_shape_left()
            if event.key == pygame.K_RIGHT:
                self.board.moving_shape_right()
            if event.key == pygame.K_UP:
                self.board.turning_shape()
            if event.key == pygame.K_RETURN:
                self.board.full_drop()
        return ""

    def render(self):
        self.screen.fill((0, 33, 55))
        self.screen.blit(self.fon, (0, 0))
        self.screen.blit(self.text_python, (325, 10))
        self.screen.blit(self.text_pygame, (325, 50))
        self.screen.blit(self.text_score, (325, 130))
        self.screen.blit(self.label_score, (325, 170))
        self.screen.blit(self.text_next_shape, (325, 210))
        self.board.render(self.screen)
        self.screen.blit(self.text_time, (325, 87))
        pygame.display.flip()