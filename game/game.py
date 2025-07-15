import random
from pathlib import Path

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
        self.TIMER = pygame.USEREVENT + 1
        self.TIME_for_TIMER = 1000
        self.time = 0
        pygame.time.set_timer(self.MYEVENTTYPE, self.TIME)
        pygame.time.set_timer(self.TIMER, self.TIME_for_TIMER)

        self.results_file = Path("data") / "results.txt"

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
        seconds = int(self.time % 60)
        hours = int(self.time // 60 // 60)
        minutes = int(self.time - seconds - hours * 60 * 60)
        out = f'{hours:02}:{minutes:02}:{seconds:02}'
        self.text_time = self.font2.render(out, True, (255, 255, 255))

    def handle_events(self, event) -> str:
        if self.board.end:
            self.func_for_end()
            return 'end'
        if event.type == self.MYEVENTTYPE:
            self.board.drop_shape()
        if event.type == self.TIMER:
            self.time += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.board.moving_shape_left()
            if event.key == pygame.K_RIGHT:
                self.board.moving_shape_right()
            if event.key == pygame.K_UP:
                self.board.turning_shape()
            if event.key == pygame.K_RETURN:
                self.board.full_drop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return "pause"
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

    def func_for_end(self):
        # обновляем поле
        self.board.score_for_end = self.board.score
        self.board.reset()
        self.board.get_shape()
        self.time = 0
