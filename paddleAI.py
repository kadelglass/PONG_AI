import pygame
from paddle import Paddle


class PaddleAI(Paddle):

    # init PaddleAI
    def __init__(self, primary, secondary, width, height, screen_bounds, ball, screen, speed):
        # call base Paddle class's init function
        super().__init__(primary, secondary, width, height, screen_bounds)

        # store the AI's custom variables needed for AI calculations
        self.ball = ball
        self.screen = screen
        self.speed = speed

    def update(self) -> None:
        # call the base update function (this function runs every time paddleB.update()
        # or all_sprites_list.update() (assuming it contains our AI paddle) is called)
        super().update()

        # if the ball is heading towards the human, go to the center and stay there
        if self.ball.velocity[0] < 0:
            # calculations for checking if the middle is above the paddle, if so move up
            if self.rect.y + (self.height / 2) > (self.screen.get_height() / 2) and not (
                    self.rect.y + (self.height / 2) <= (self.screen.get_height() / 2) + self.speed):
                self.move_up(self.speed)
            # calculations for checking if the middle is below the paddle, if so move down
            elif self.rect.y + (self.height / 2) < (self.screen.get_height() / 2) and not (
                    self.rect.y + (self.height / 2) >= (self.screen.get_height() / 2) - self.speed):
                self.move_down(self.speed)
        # if the ball is heading towards the AI (and past the halfway point), align the paddle's center with the
        # ball's center
        elif self.ball.velocity[0] > 0 and self.ball.rect.x >= self.screen.get_width() / 2:
            # first check if the y distance (absolute value of (ball center y - paddle center y))
            # from the ball is greater than the speed plus some. this makes it so that
            # the AI is smoother and doesn't wildly shake in an attempt to align itself with the ball perfectly
            # down to the pixel (it can't do that because its speed is greater than 1, but it thinks it can)
            if abs((self.ball.rect.y + (self.ball.height / 2)) - (self.rect.y + (self.height / 2))) >= self.speed + 1:
                # if the ball's center is below the paddle's center, move down
                if self.ball.rect.y + (self.ball.height / 2) > self.rect.y + (self.height / 2):
                    self.move_down(self.speed)
                # if the ball's center is above the paddle's center, move up
                elif self.ball.rect.y + (self.ball.height / 2) < self.rect.y + (self.height / 2):
                    self.move_up(self.speed)
