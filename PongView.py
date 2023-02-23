import pygame

class PongView:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.Font(None, 36)

    def draw_ball(self, ball):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(ball.x), int(ball.y)), ball.radius)

    def draw_paddle(self, paddle):
        pygame.draw.rect(self.screen, (255, 255, 255), (paddle.x, paddle.y, paddle.width, paddle.height))

    def draw_scores(self, score):
        score1_text = self.font.render(str(score.score1), True, (255, 255, 255))
        score2_text = self.font.render(str(score.score2), True, (255, 255, 255))
        score1_rect = score1_text.get_rect()
        score2_rect = score2_text.get_rect()
        score1_rect.centerx = self.screen.get_rect().centerx - 50
        score2_rect.centerx = self.screen.get_rect().centerx + 50
        score1_rect.centery = 10
        score2_rect.centery = 10
        self.screen.blit(score1_text, score1_rect)
        self.screen.blit(score2_text, score2_rect)

    def update(self, ball, paddle1, paddle2, score):
        self.screen.fill((0, 0, 0))
        self.draw_ball(ball)
        self.draw_paddle(paddle1)
        self.draw_paddle(paddle2)
        self.draw_scores(score)
        pygame.display.update()
