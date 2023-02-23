import pygame
import sys
from DynamicAI import AIDynamic

class PongController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.opponent = AIDynamic(paddle = self.model.paddle1, ball = self.model.ball)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                elif event.key == pygame.K_UP:
                    self.model.paddle2.move_up_flag = True
                elif event.key == pygame.K_DOWN:
                    self.model.paddle2.move_down_flag = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.model.paddle2.move_up_flag = False
                elif event.key == pygame.K_DOWN:
                    self.model.paddle2.move_down_flag = False

    def update(self):
        self.model.ball.move()
        self.model.ball.check_wall_collision(self.view.screen_height)
        self.model.ball.check_paddle_collision(self.model.paddle1, self.model.paddle2)
        self.model.score.update_score(self.model.ball, self.view.screen_width, self.view.screen_height)
        self.model.paddle1.update_position(self.view.screen_height)
        self.opponent.move()
        self.model.paddle2.update_position(self.view.screen_height)
        self.view.update(self.model.ball, self.model.paddle1, self.model.paddle2, self.model.score)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.handle_events()
            self.update()
