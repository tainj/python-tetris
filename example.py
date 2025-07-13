import pygame
import sys
import time

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Имитация загрузки")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Параметры прогресс-бара
progress_width = 600
progress_height = 30
progress_x = (WIDTH - progress_width) // 2
progress_y = (HEIGHT - progress_height) // 2

def draw_progress_bar(current, total):
    progress = current / total
    filled_width = int(progress_width * progress)
    pygame.draw.rect(screen, WHITE, (progress_x, progress_y, progress_width, progress_height), 2)
    pygame.draw.rect(screen, BLUE, (progress_x, progress_y, filled_width, progress_height))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Loading... {int(progress * 100)}%", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, progress_y - 30))
    screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True
    current_progress = 0
    total_progress = 100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_progress_bar(current_progress, total_progress)

        if current_progress < total_progress:
            current_progress += 1
            time.sleep(0.07)  # Имитация задержки

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()