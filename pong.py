import pygame
pygame.init()

FPS = 60
WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

WHITE = (255,255,255)
BLACK = (0,0,0)

class Paddle:
    COLORO = WHITE
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.widt = width
        self.height = height





def draw(win):
    win.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock(WINDOW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == 'main':
    main()