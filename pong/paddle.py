import pygame


class Paddle:
    VELOCITY = 50
    COLOR = WHITE = (255,255,255)


    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    
    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        elif up ==2:
            self.y = 0
        else:
            self.y += self.VELOCITY


    def reset(self):
        self.x = self.original_x
        self.y = self.original_y