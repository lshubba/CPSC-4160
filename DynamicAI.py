

class AIDynamic:
    def __init__(self, paddle, ball):
        self.paddle = paddle
        self.ball = ball

    def move(self):
        if self.ball.speed_x < 0:
            if self.ball.y < self.paddle.y:
                self.paddle.move_up()
            if self.ball.y > self.paddle.y + self.paddle.y:
                self.paddle.move_down()

        """if self.ball.speed_x < 0:
            if self.ball.y > self.y + self.paddle.y / 2:
                self.paddle.move_down()
        else:
            if self.ball.y < self.y + self.paddle.y / 2:
                self.paddle.move_up() """