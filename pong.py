import pygame
pygame.init()

FPS = 10
WIDTH, HEIGHT = 750, 550
PADDLE_WIDTH, PADDLE_HEIGHT = 50, 150
BALL_WIDTH, BALL_HEIGHT = 50, 50
WIN_SCORE = 10

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")
SCORE_FONT = pygame.font.SysFont("Cambria Bold", 100)

WHITE = (255,255,255)
BLACK = (0,0,0)
ALMOST_BLACK = (30, 30, 30)

class Paddle:
    COLOR = WHITE
    VELOCITY = 50


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
        else:
            self.y += self.VELOCITY


    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VELOCITY = 50
    COLOR = WHITE

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
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
        

def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)
    blockSize = 50
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(win, ALMOST_BLACK, rect, 1)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (200 + 6, 50))
    win.blit(right_score_text, (500 + 6, 50))
    ball.draw(win)
    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    def set_vel(paddle):
        ball.x_vel *= -1
        difference_in_y = paddle.y - ball.y
        if difference_in_y == 0:
            ball.y_vel = -1 * ball.MAX_VELOCITY

        elif difference_in_y == -50:
            ball.y_vel = 0

        elif difference_in_y == -100:
            ball.y_vel = ball.MAX_VELOCITY


    if ball.y + ball.height >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y  <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.width <= left_paddle.x:
                set_vel(left_paddle)
                
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.width >= right_paddle.x:
                set_vel(right_paddle)


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up=True)

    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELOCITY + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP]and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(up=True)

    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELOCITY + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()
    left_paddle = Paddle(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
    left_score = 0
    right_score = 0 
    while run:
        pygame.time.delay(50)
        clock.tick(FPS)
        draw(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
        
        won = False
        if left_score >= WIN_SCORE:
            won = True
        elif right_score >= WIN_SCORE:
            won = True
            
        if won:
            pygame.display.update()
            pygame.time.delay(3000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = right_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()