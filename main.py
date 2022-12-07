import pygame
from simulation import Simulation
from pong import Pong
from AI import SimpleAi



EPOCH = 1
WIN_SCORE = 10
WIDTH, HEIGHT = 850, 650
FPS = 10
VELOCITY = 50

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
ai = SimpleAi()
env = Pong(WINDOW, WIDTH, HEIGHT, VELOCITY, ai_right = ai)
"""states = [(ball position), (right paddle), (left paddle)] """
states, states_hash = env.get_all_states()
policy = env.get_policy(states)
sim1 = Simulation(FPS, env, ai, WIN_SCORE)
for _ in range(EPOCH):
    sim1.run()
