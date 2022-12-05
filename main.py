import pygame
from simulation import Simulation
from pong import Pong
from AI import SimpleAi



EPOCH = 1
WIN_SCORE = 10
WIDTH, HEIGHT = 850, 650

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
ai = SimpleAi()
env = Pong(WINDOW, WIDTH, HEIGHT, ai_right = ai)
states, states_hash = env.get_all_states()
sim1 = Simulation(env, ai, WIN_SCORE)
for _ in range(EPOCH):
    sim1.run()
