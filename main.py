import pygame
from simulation import Simulation
from pong import Pong
from AiSimpleinPlace import SimpleAi
from AiSimpleinPlace import InPlace
from AiSimpleinPlace import RandomAi



EPOCH = 1000
WIN_SCORE = 5
WIDTH, HEIGHT = 350, 350
WIDTH, HEIGHT = 750, 750
FPS = 1000
VELOCITY = 50

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
env = Pong(WINDOW, WIDTH, HEIGHT, VELOCITY, WIN_SCORE)
random_ai = RandomAi()
simple_ai = SimpleAi()
states, states_hash = env.get_all_states()
print('State:', len(states))

tree = env.get_tree(states)
policy = env.get_policy(states)
in_place_ai = InPlace(tree, env, policy)
best_strategy_tree = in_place_ai.value_iteration(states, 0.9, 0.0001)
print('done')

env.set_left_ai(in_place_ai)
env.set_right_ai(in_place_ai)
sim1 = Simulation(FPS, env, WIN_SCORE)
for _ in range(EPOCH):
    sim1.run()
