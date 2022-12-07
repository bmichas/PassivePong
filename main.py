import pygame
from simulation import Simulation
from pong import Pong
from AiSimpleinPlace import SimpleAi
from AiSimpleinPlace import InPlace
from AiSimpleinPlace import RandomAi



EPOCH = 10
WIN_SCORE = 5
WIDTH, HEIGHT = 550, 550
# WIDTH, HEIGHT = 750, 750
FPS = 100
VELOCITY = 50

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
ai_left = SimpleAi()
ai_left = RandomAi()
env = Pong(WINDOW, WIDTH, HEIGHT, VELOCITY, WIN_SCORE)
"""states = [(ball position), (right paddle), (left paddle)] """
states, states_hash = env.get_all_states()
tree = env.get_tree(states)
print('State:', len(states))
policy = env.get_policy(states)
ai_right = InPlace(tree, env, policy)
best_strategy_tree = ai_right.value_iteration(states, 0.9, 0.0001)
print('done')
env.set_left_ai(ai_right)
env.set_right_ai(ai_left)
sim1 = Simulation(FPS, env, ai_right, WIN_SCORE)
for _ in range(EPOCH):
    sim1.run()
