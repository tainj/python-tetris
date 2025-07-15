import pygame
from game.states import State


class GameOver(State):
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.score = board.score_for_end
        self.font = pygame.font.SysFont("Arial", 50)
        self.small_font = pygame.font.SysFont("Arial", 30)

        # Тексты
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.play_again_text = self.small_font.render("Play Again", True, (255, 255, 255))
        self.menu_text = self.small_font.render("Main Menu", True, (255, 255, 255))
        self.score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.game_over_rect = pygame.Rect(75, 160, 350, 260)
        self.button_width = 200
        self.button_height = 50
        self.play_again_button = pygame.Rect(150, 270, self.button_width, self.button_height)
        self.menu_button = pygame.Rect(150, 340, self.button_width, self.button_height)

    def handle_events(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.play_again_button.collidepoint(mouse_pos):  # клик на "Play Again"
                return "game"  # перезапуск игры
            elif self.menu_button.collidepoint(mouse_pos):  # клик на "Main Menu"
                return "menu"  # переход в меню

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # перезапуск игры по нажатию SPACE
                return "game"

    def update(self):
        pass  # в завершении игры не нужно обновлять игровую логику

    def render(self):
        # рисуем прямоугольник завершения игры
        pygame.draw.rect(self.screen, (0, 33, 55), self.game_over_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.game_over_rect, 2)

        # рисуем текст "Game Over"
        game_over_rect = self.game_over_text.get_rect(center=(500 // 2, 190))
        self.screen.blit(self.game_over_text, game_over_rect)

        # рисуем текст счёта
        self.score = self.board.score_for_end
        self.score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = self.score_text.get_rect(center=(500 // 2, 240))
        self.screen.blit(self.score_text, score_rect)

        # рисуем кнопку "Play Again"
        pygame.draw.rect(self.screen, (0, 33, 55), self.play_again_button)  # Зелёный цвет
        pygame.draw.rect(self.screen, (255, 255, 255), self.play_again_button, 2)  # Белая граница
        play_again_text_rect = self.play_again_text.get_rect(center=self.play_again_button.center)
        self.screen.blit(self.play_again_text, play_again_text_rect)

        # рисуем кнопку "Main Menu"
        pygame.draw.rect(self.screen, (0, 33, 55), self.menu_button)  # Красный цвет
        pygame.draw.rect(self.screen, (255, 255, 255), self.menu_button, 2)  # Белая граница
        menu_text_rect = self.menu_text.get_rect(center=self.menu_button.center)
        self.screen.blit(self.menu_text, menu_text_rect)

        pygame.display.flip()