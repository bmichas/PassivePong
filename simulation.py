import pygame

class Simulation:
    def __init__(self, fps ,game, ai, win_score) -> None:
        self.fps = fps
        self.enviroment = game
        self.ai = ai
        self.win_score = win_score
        self.clock = pygame.time.Clock()


    def run(self):
        run = True
        while run:
            pygame.time.delay(50)
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
     
            # current_state = self.enviroment.get_current_state()
            # actions = self.enviroment.get_possible_actions(current_state)
            # for action in actions:
            #     next_states = self.enviroment.get_next_states(current_state, action)
            #     print("State: " + str(current_state) + " action: " + str(action) + " " + "list of possible next states: ", str(next_states))

            
            self.enviroment.step()
            print(self.enviroment.get_reward())
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