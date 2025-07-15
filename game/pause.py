import pygame
from game.states import State


class Pause(State):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 50)
        self.small_font = pygame.font.SysFont("Arial", 30)

        # тексты
        self.pause_text = self.font.render("Paused", True, (255, 255, 255))
        self.resume_text = self.small_font.render("Continue", True, (255, 255, 255))
        self.menu_text = self.small_font.render("Main Menu", True, (255, 255, 255))

        # параметры прямоугольника паузы
        self.pause_rect = pygame.Rect(100, 200, 300, 220)  # прямоугольник для паузы
        self.button_width = 200
        self.button_height = 50
        self.resume_button = pygame.Rect(150, 270, self.button_width, self.button_height)  # кнопка "Continue"
        self.menu_button = pygame.Rect(150, 340, self.button_width, self.button_height)  # кнопка "Main Menu"

    def handle_events(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.resume_button.collidepoint(mouse_pos):
                return "game"  # возврат в игру
            elif self.menu_button.collidepoint(mouse_pos):
                return "menu" # переход в меню

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # возврат в игру по нажатию SPACE
                return "game"

    def update(self):
        pass  # в паузе не нужно обновлять игровую логику

    def render(self):
        # Рисуем прямоугольник паузы
        pygame.draw.rect(self.screen, (0, 33, 55), self.pause_rect)  # Синий цвет
        pygame.draw.rect(self.screen, (255, 255, 255), self.pause_rect, 2)  # Белая граница

        # Рисуем текст "Paused"
        text_rect = self.pause_text.get_rect(center=(500 // 2, 240))
        self.screen.blit(self.pause_text, text_rect)

        # Расстояние между кнопками
        button_spacing = 20  # Отступ между кнопками

        # Позиции кнопок
        self.resume_button.x = 150  # Позиция кнопки "Continue"
        self.menu_button.x = 150  # Позиция кнопки "Main Menu"

        # Рисуем кнопку "Continue"
        pygame.draw.rect(self.screen, (0, 33, 55), self.resume_button)  # Голубой цвет
        pygame.draw.rect(self.screen, (255, 255, 255), self.resume_button, 2)  # Белая граница
        resume_text_rect = self.resume_text.get_rect(center=self.resume_button.center)
        self.screen.blit(self.resume_text, resume_text_rect)

        # Рисуем кнопку "Main Menu"
        pygame.draw.rect(self.screen, (0, 33, 55), self.menu_button)  # Синий цвет (оттенок)
        pygame.draw.rect(self.screen, (255, 255, 255), self.menu_button, 2)  # Белая граница
        menu_text_rect = self.menu_text.get_rect(center=self.menu_button.center)
        self.screen.blit(self.menu_text, menu_text_rect)

        pygame.display.flip()  # Обновляем экран