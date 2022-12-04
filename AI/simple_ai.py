class SimpleAi:
    def __init__(self) -> None:
        pass

    def move_paddle(self, paddle_y, ball_y):
        ratio = paddle_y - ball_y
        if abs(ratio) == 50 or abs(ratio) == 100 or abs(ratio) == 150:
            return 2
        else: 
            if ratio < 0:
                return False
            else:
                return True

    def flag(self, flag = True):
        return flag

    