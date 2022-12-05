import pygame
import random

class Ball:
    MAX_VELOCITY = 100
    COLOR = WHITE = (255,255,255)

    def __init__(self, x, y, width, height) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0

    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    
    def reset(self):
        y_vel_lst = [-50,0,50]
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = random.choice(y_vel_lst)
        self.x_vel *= -1