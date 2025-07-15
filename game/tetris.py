import pygame
from game.game import Game
from game.gameover import GameOver
from game.loading import Loading
from game.menu import Menu
from game.pause import Pause


class Tetris:
    def __init__(self):
        pygame.init()
        self.width, self.height = 500, 620
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.game = Game(screen=self.screen)
        self.states = {
            "load": Loading(screen=self.screen),
            "menu": Menu(screen=self.screen),
            "game": self.game,
            "pause": Pause(screen=self.screen),
            "end": GameOver(screen=self.screen, board=self.game.board)
        }

        # инициализация дополнительных переменных

        self.current_state = self.states["load"]

    def run(self):
        pygame.display.set_caption('Tetris 1.1')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                result = self.current_state.handle_events(event)
                if result:
                    self.current_state = self.states[result]
                    if result == "menu":
                        self.game.func_for_end()
            self.current_state.update()
            self.current_state.render()
            self.clock.tick(60)

        pygame.quit()