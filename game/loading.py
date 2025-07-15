import time
import pygame
from game.states import State
from game.utils import load_image


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Loading(State):
    def __init__(self, screen, width=500, height=620):
        self.screen = screen
        self.width = width
        self.height = height
        self.progress_width = 480
        self.progress_height = 30
        self.progress_x = (self.width - self.progress_width) // 2
        self.progress_y = (self.height - self.progress_height) // 2

        self.current_progress = 0
        self.total_progress = 100
        self.progress = 0
        self.filled_width = 0

        self.loading_screen = pygame.transform.scale(load_image("loading_screen.jpg"), (500, 620))

    def render(self):
        self.progress = self.current_progress / self.total_progress
        self.filled_width = int(self.progress_width * self.progress)
        pygame.draw.rect(self.screen, WHITE, (self.progress_x, self.progress_y, self.progress_width, self.progress_height), 2)
        pygame.draw.rect(self.screen, WHITE, (self.progress_x, self.progress_y, self.filled_width, self.progress_height))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Loading... {int(self.progress * 100)}%", True, WHITE)
        text_rect = text.get_rect(center=(self.width // 2, self.progress_y - 30))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def handle_events(self, event) -> str:
        if self.current_progress < self.total_progress:
            self.current_progress += 5
            time.sleep(0.03)
            return ""
        return "menu"

    def update(self):
        self.screen.blit(self.loading_screen, (0, 0))