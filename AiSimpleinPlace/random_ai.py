import random
class RandomAi:
    def __init__(self) -> None:
        pass


    def move_paddle(self, paddle_y, ball_y):
        lst = [True, 2, False]
        return random.choice(lst)


    def flag(self, flag = True):
        return flag
    