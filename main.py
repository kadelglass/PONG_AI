# Import the pygame library and initialize the pygame (engine).
import pygame
from paddle import Paddle
from paddleAI import PaddleAI
from ball import Ball


def draw_middle_line(screen, PRIMARY):
    for i in range(1, int(screen.get_height() / 5)):
        if i != 5:
            pygame.draw.rect(screen, PRIMARY, [(screen.get_width() / 2) - 5, (i * 50), 10, 10])
        else:
            pygame.draw.rect(screen, PRIMARY, [(screen.get_width() / 2) - 5, (i * 50), 10, 10])


def main():
    pygame.init()
    pygame.mixer.init()

    # define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = pygame.Color("#072b5f")
    NAVY_BLUE = (8, 21, 57)
    DARKER_GRAY = (50, 50, 50)
    DARK_GRAY = (100, 100, 100)
    GRAY = (150, 150, 150)
    LIGHT_GRAY = (200, 200, 200)
    LIGHTER_GRAY = (225, 225, 225)
    YELLOW = pygame.Color("#f5d13b")
    GREENISH = (243, 255, 243)
    PURPLISH = (7, 0, 10)

    # choose colors
    SECONDARY = PURPLISH
    PRIMARY = GREENISH

    # Open a new window for our game
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PYGAME PONG")
    sound = pygame.mixer.Sound("sound.wav")
    soundMissedShot = pygame.mixer.Sound("missedshot.wav")

    # screen bounds init
    screenBounds = (16, screen.get_height() - 14)

    # player offset init
    pOffset = 20
    pSpeed = 5

    # enemy offset init (difficulty, higher number = higher difficulty because the paddle will go faster)
    aiSpeed = 5

    # ball init
    ball_speed = 3
    ball = Ball(PRIMARY, SECONDARY, 10, 10, ball_speed, screenBounds)
    ball.rect.x = (screen.get_width() / 2) - (ball.width / 2)
    ball.rect.y = (screen.get_height() / 2) - (ball.height / 2)

    paddleB = PaddleAI(PRIMARY, SECONDARY, 10, 100, screenBounds, ball, screen, aiSpeed)
    paddleB.rect.x = screen.get_width() - pOffset - 10
    paddleB.rect.y = (screen.get_height() / 2) - 50

    paddleA = Paddle(PRIMARY, SECONDARY, 10, 100, screenBounds)
    paddleA.rect.x = pOffset
    paddleA.rect.y = (screen.get_height() / 2) - 50

    # Create a variable that is a list that contains our sprites.
    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # Variable to exit game
    carryOn = True

    # The clock controlling the screen updates
    clock = pygame.time.Clock()

    # Initialize player scores
    scoreA = 0
    scoreB = 0
    scoreNeeded = 11

    gameOn = True

    # |-------------MAIN GAME LOOP--------------------|
    while carryOn:
        # ------MAIN EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()
        # PADDLE A MOVES!
        if keys[pygame.K_w]:
            paddleA.move_up(pSpeed)
        if keys[pygame.K_s]:
            paddleA.move_down(pSpeed)

        if keys[pygame.K_r] and not gameOn:
            main()

        if gameOn:

            # Game Logic Goes Here
            all_sprites_list.update()

            # Check if ball is touching any of the 4 walls:
            if ball.rect.x >= 690:
                soundMissedShot.play()
                scoreA += 1
                ball.rect.x = 350

                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                soundMissedShot.play()
                scoreB += 1
                ball.rect.x = 350
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y >= screenBounds[1] - ball.height:
                ball.velocity[1] = -ball.velocity[1]
                sound.play()

            elif ball.rect.y <= screenBounds[0]:
                ball.velocity[1] = -ball.velocity[1]
                sound.play()

            # paddles
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                ball.bounce()
                sound.play()

            # ---Drawing on the screen goes here
            screen.fill(BLACK)
            # draw top and bottom lines
            pygame.draw.line(screen, PRIMARY, (0, 5), (screen.get_width(), 5), 20)
            pygame.draw.line(screen, PRIMARY, (0, screen.get_height() - 5),
                             (screen.get_width(), screen.get_height() - 5),
                             20)
            draw_middle_line(screen, PRIMARY)
            all_sprites_list.draw(screen)

            # Display Score
            font = pygame.font.SysFont("Showcard Gothic", 74)
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250, 10 + screenBounds[0]))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (420, 10 + screenBounds[0]))
            # Check for game over with a Score of x
            if scoreA == scoreNeeded or scoreB == scoreNeeded:
                gameOn = False
                screen.fill(BLACK)
                pygame.display.flip()
                fontGameOver = pygame.font.SysFont("Showcard Gothic", 25)

                if scoreA == 3:
                    textGameOver = fontGameOver.render("Player A Wins!" + "  Press R To Play Again!", 1, WHITE)
                    textRect = textGameOver.get_rect()
                    textRect.center = screen.get_rect().center
                    screen.blit(textGameOver, textRect)
                if scoreB == 3:
                    textGameOver = fontGameOver.render("Player B Wins!" + "  Press R To Play Again!", 1, WHITE)
                    textRect = textGameOver.get_rect()
                    textRect.center = screen.get_rect().center
                    screen.blit(textGameOver, textRect)

                pygame.display.flip()
                pygame.time.delay(2000)

        # ---Update the screen with what we drew above
        pygame.display.flip()

        #  ---Frames per second (FPS) using our clock
        clock.tick(60)

    # Code that runs when the user exits the game
    pygame.quit()


if __name__ == '__main__': main()
