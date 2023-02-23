import pygame
import random

class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 10
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.color = (255, 255, 255)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def check_wall_collision(self, screen_height):
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.speed_y = -self.speed_y
    
    def check_paddle_collision(self, paddle1, paddle2):
        if self.x - self.radius <= paddle1.x + paddle1.width and paddle1.y <= self.y <= paddle1.y + paddle1.height:
            self.speed_x = abs(self.speed_x)
        elif self.x + self.radius >= paddle2.x and paddle2.y <= self.y <= paddle2.y + paddle2.height:
            self.speed_x = -abs(self.speed_x)

class Paddle:
    def __init__(self, x, y):
        self.width = 10
        self.height = 50
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.speed = 5
        self.move_up_flag = False
        self.move_down_flag = False
    
    def move_up(self):
        self.y -= self.speed
    
    def move_down(self):
        self.y += self.speed

    def update_position(self, screen_height):
        if self.move_up_flag:
            self.move_up()
        if self.move_down_flag:
            self.move_down()
        self.y = max(0, min(self.y, screen_height  - self.height))

class Score:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
    
    def update_score(self, ball, screen_width, screen_height):
        if ball.x - ball.radius <= 0:
            self.score2 += 1
            ball.__init__(screen_width, screen_height)
        elif ball.x + ball.radius >= screen_width:
            self.score1 += 1
            ball.__init__(screen_width, screen_height)

class PongModel:
    def __init__(self, screen_width, screen_height):
        self.ball = Ball(screen_width, screen_height)
        self.paddle1 = Paddle(10, screen_height // 2 - 25)
        self.paddle2 = Paddle(screen_width - 20, screen_height // 2 - 25)
        self.score = Score()
