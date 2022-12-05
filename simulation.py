import pygame

class Simulation:
    def __init__(self, game, ai, win_score) -> None:
        self.enviroment = game
        self.ai = ai
        self.win_score = win_score
        self.clock = pygame.time.Clock()


    def run(self):
        run = True
        while run:
            pygame.time.delay(50)
            self.clock.tick(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.enviroment.step()
            self.enviroment.draw()
            won = False
            if self.enviroment.left_score >= self.win_score:
                won = True
            elif self.enviroment.right_score >= self.win_score:
                won = True

            if won:
                self.enviroment.reset()
                run = False

            pygame.display.update()