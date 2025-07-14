import pygame
from game.utils import load_image


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.loading_screen = pygame.transform.scale(load_image("loading_screen.jpg"), (500, 620))  # Загружаем и масштабируем фон
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)  # Уменьшил шрифт для кнопки
        self.button_play = pygame.Rect(150, 300, 200, 50)  # Новая позиция и размер кнопки
        self.colors = {
            "button": (0, 128, 255),  # Цвет кнопки
            "text": (255, 255, 255)   # Цвет текста
        }

    def render(self):
        self.screen.blit(self.loading_screen, (0, 0))  # Рисуем фон
        self.draw()
        pygame.display.flip()

    def draw(self):
        # Рисуем кнопку
        pygame.draw.rect(self.screen, self.colors["button"], self.button_play)

        # Текст для кнопки
        text_play = self.font.render("Играть", True, self.colors["text"])
        self.screen.blit(text_play, (self.button_play.x + 50, self.button_play.y + 10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play.collidepoint(event.pos):
                        return "play"  # Возвращаем действие "play" при нажатии

            self.render()
            self.clock.tick(30)