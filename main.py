import pygame
from pong import Game
from AI import SimpleAi


epoch = 2
win_score = 3
width, height = 850, 650
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game = Game(window, width, height)
ai = SimpleAi()

run = True
while run:
    pygame.time.delay(50)
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)

    if keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)

    if ai.flag():
        move = ai.move_paddle(game.right_paddle.y, game.ball.y)
        # UP == True, if UP==2: stay
        game.move_paddle(left=False, up=move)
    else:
        print(game.right_paddle.y, game.ball.y)
        if keys[pygame.K_UP]:
            game.move_paddle(left=False, up=True)

        if keys[pygame.K_DOWN]:
            game.move_paddle(left=False, up=False)

    game.loop()
    game.draw()
    won = False
    if game.left_score >= win_score:
        won = True
    elif game.right_score >= win_score:
        won = True

    if won:
        game.reset()
        run = False

    pygame.display.update()

