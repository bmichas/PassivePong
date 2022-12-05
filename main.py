import pygame
from pong import Game
from AI import SimpleAi



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
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.enviroment.move_paddle(left=True, up=True)

            if keys[pygame.K_s]:
                self.enviroment.move_paddle(left=True, up=False)

            if self.ai.flag():
                move = self.ai.move_paddle(self.enviroment.right_paddle.y, self.enviroment.ball.y)
                # UP == True, if UP==2: stay
                self.enviroment.move_paddle(left=False, up=move)
            else:
                print(self.enviroment.right_paddle.y, self.enviroment.ball.y)
                if keys[pygame.K_UP]:
                    self.enviroment.move_paddle(left=False, up=True)

                if keys[pygame.K_DOWN]:
                    self.enviroment.move_paddle(left=False, up=False)

            self.enviroment.loop()
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



epoch = 2
win_score = 3
width, height = 850, 650
window = pygame.display.set_mode((width, height))
game = Game(window, width, height)
ai = SimpleAi()
sim1 = Simulation(game, ai, win_score)
for _ in range(epoch):
    sim1.run()


        





