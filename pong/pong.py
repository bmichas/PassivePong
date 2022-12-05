import pygame
from pong.paddle import Paddle
from pong.ball import Ball
pygame.init()


PADDLE_WIDTH, PADDLE_HEIGHT = 50, 150
BALL_WIDTH, BALL_HEIGHT = 50, 50


class Pong:
    SCORE_FONT = pygame.font.SysFont("Cambria Bold", 100)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    ALMOST_BLACK = (30, 30, 30)
    

    def __init__(self, window, window_width, window_height, ai_left = False, ai_right = False):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.left_paddle = Paddle(50, window_height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(window_width - 50 - PADDLE_WIDTH, window_height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(window_width // 2 - BALL_WIDTH // 2, window_height // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
        self.left_paddle_position = (self.left_paddle.x, self.left_paddle.y)
        self.right_paddle_position = (self.right_paddle.x, self.right_paddle.y)
        self.ai_left = ai_left
        self.ai_right = ai_right
        self.left_score = 0
        self.right_score = 0
        self.left_hit_count = 0
        self.right_hit_count = 0
        self.counter = 0

    
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

        # Collision with board
        if ball.y + ball.height >= self.window_height:
            ball.y_vel *= -1
        elif ball.y <= 0:
            ball.y_vel *= -1

        # Collision with paddles
        if ball.x_vel < 0:
            # Left
            if ball.y >= left_paddle.y and ball.y < left_paddle.y + left_paddle.height:
                if ball.x - ball.width <= left_paddle.x:
                    set_vel(left_paddle)
                    self.left_hit_count += 1

        else:
            # right
            if ball.y >= right_paddle.y and ball.y < right_paddle.y + right_paddle.height:
                if ball.x + ball.width >= right_paddle.x:
                    set_vel(right_paddle)
                    self.right_hit_count += 1


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


    def move_left_paddle(self, up=True):
        if up and self.left_paddle.y - Paddle.VELOCITY < 0:
            return False
        if not up and self.left_paddle.y + PADDLE_HEIGHT >= self.window_height:
            return False

        if up == 2:
            return 2
  
        self.left_paddle.move(up)
        return True
        

    def move_right_paddle(self, up=True):
        if up and self.right_paddle.y - Paddle.VELOCITY < 0:
            return False
        if not up and self.right_paddle.y + PADDLE_HEIGHT  >= self.window_height:
            return False

        if up == 2:
            return 2

        self.right_paddle.move(up)
        return True

    def step(self):
        keys = pygame.key.get_pressed()
        if self.ai_left:
            pass
        else:
            if keys[pygame.K_w]:
                self.move_left_paddle(up=True)

            if keys[pygame.K_s]:
                self.move_left_paddle(up=False)

        move = self.ai_right.move_paddle(self.right_paddle.y, self.ball.y)
        # UP == True, if UP==2: stay
        prev_left_position = self.left_paddle_position
        prev_right_position = self.right_paddle_position
        self.move_right_paddle(move)
        self.ball.move()
        self._handle_collision(self.ball, self.left_paddle, self.right_paddle)
        print('BALL:', self.ball.x, self.ball.y, self.ball.x_vel, self.ball.y_vel)
        print('LeftPaddle:', self.left_paddle.x, self.left_paddle.y, self.left_hit_count)
        print('RightPaddle:', self.right_paddle.x, self.right_paddle.y, self.right_hit_count)
        
        if prev_left_position == self.left_paddle_position:
            self.counter += 1
            if self.counter == 200:
                self.ball.reset()
                self.counter = 0

        if prev_right_position == self.right_paddle_position:
            self.counter += 1
            if self.counter == 200:
                self.ball.reset()
                self.counter = 0

        
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
        self.left_hit_count = 0
        self.right_hit_count = 0
        self.counter = 0