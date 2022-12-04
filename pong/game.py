import pygame
from pong.paddle import Paddle
from pong.ball import Ball
pygame.init()


FPS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 50, 150
BALL_WIDTH, BALL_HEIGHT = 50, 50
WIN_SCORE = 10


class Game:
    SCORE_FONT = pygame.font.SysFont("Cambria Bold", 100)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    ALMOST_BLACK = (30, 30, 30)
    

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.left_paddle = Paddle(50, window_height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(window_width - 50 - PADDLE_WIDTH, window_height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(window_width // 2 - BALL_WIDTH // 2, window_height // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
        self.left_score = 0
        self.right_score = 0

    
    def _draw_score(self):
        left_score_text = self.SCORE_FONT.render(f"{self.left_score}", 1, self.WHITE)
        right_score_text = self.SCORE_FONT.render(f"{self.right_score}", 1, self.WHITE)
        self.window.blit(left_score_text, (200 + 6, 50))
        self.window.blit(right_score_text, (500 + 6, 50))

    def _handle_collision(self, ball, left_paddle, right_paddle):
        def set_vel(paddle):
            ball.x_vel *= -1
            difference_in_y = paddle.y - ball.y
            if difference_in_y == 0:
                ball.y_vel = -1 * ball.MAX_VELOCITY

            elif difference_in_y == -50:
                ball.y_vel = 0

            elif difference_in_y == -100:
                ball.y_vel = ball.MAX_VELOCITY


        if ball.y + ball.height >= self.window_height:
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


    def draw(self, draw_score = True):
        self.window.fill(self.BLACK)
        blockSize = 50
        for x in range(0, self.window_width, blockSize):
            for y in range(0, self.window_height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.window, self.ALMOST_BLACK, rect, 1)

        if draw_score:
            self._draw_score()

        self.ball.draw(self.window)
        paddles = [self.left_paddle, self.right_paddle]
        for paddle in paddles:
            paddle.draw(self.window)
        
        self.ball.draw(self.window)


    def move_paddle(self, left=True, up=True):
        if left:
            if up and self.left_paddle.y - Paddle.VELOCITY < 0:
                return False
            if not up and self.left_paddle.y + PADDLE_HEIGHT > self.window_height:
                return False
            self.left_paddle.move(up)
        elif up == 2:
            return 2
        else:
            if up and self.right_paddle.y - Paddle.VELOCITY < 0:
                return False
            if not up and self.right_paddle.y + PADDLE_HEIGHT  > self.window_height:
                return False
            self.right_paddle.move(up)

        return True

    def loop(self):
        self.ball.move()
        self._handle_collision(self.ball, self.left_paddle, self.right_paddle)
        if self.ball.x < 0:
            self.ball.reset()
            self.right_score += 1
        elif self.ball.x > self.window_width:
            self.ball.reset()
            self.left_score += 1



    def reset(self):
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0