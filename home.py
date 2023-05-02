# necessary imports
import pygame
import os
import sys
from objects import Player, Enemy, Power
from button import Button
from dungeon import func2
from bedroom import func1
from scienceLab import func3


# game loop function (allows interaction and changes in physics)

def main(WIN, player):
    pygame.font.init()
    clock = pygame.time.Clock()  # keeps track of time of game
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    run = True
    FPS = 60  # checks physics 60 frames per second
    finished = False
    finished_count = 0
    velocity_y = 5  # higher velocity for lower clock-speed; how many pixels moved per frame
    velocity_x = 8
    lives_font = pygame.font.SysFont("comicsans", 40)
    end_font = pygame.font.SysFont("comicsans", 100)

    # load images (creates surfaces)

    imgDir = "gameImages"
    # # background images

    doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
    doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))

    # # Button images
    one = pygame.image.load(os.path.join(imgDir, "one.png"))
    one = pygame.transform.scale(one, (WIDTH / 8, HEIGHT / 8))
    two = pygame.image.load(os.path.join(imgDir, "two.png"))
    two = pygame.transform.scale(two, (WIDTH / 8, HEIGHT / 8))
    three = pygame.image.load(os.path.join(imgDir, "three.png"))
    three = pygame.transform.scale(three, (WIDTH / 8, HEIGHT / 8))

    door_1 = Button(200, 40, one)
    door_2 = Button(0.5 * WIDTH - 0.5 * two.get_width(), 40, two)
    door_3 = Button(700, 40, three)

    def redraw_window(finish):
        # # created background
        WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        player.draw(WIN)
        intro_text = lives_font.render("Pick a Door", True, (255, 250, 250))
        WIN.blit(intro_text, (0.5 * WIDTH - 0.5 * intro_text.get_width(), 0))

        door_1.draw(WIN, func1, player)
        door_2.draw(WIN, func2, player)
        door_3.draw(WIN, func3, player)

        lives_label = lives_font.render(f"Lives: {player.lives}", True, (255, 0,0))
        WIN.blit(lives_label, (0, 0))

        if finish:
            finished_label = end_font.render("To be continued...?!?", True, (255, 0, 0))
            WIN.blit(finished_label,
                     (0.5 * WIDTH - 0.5 * finished_label.get_width(), 0.5 * HEIGHT - 0.5 * finished_label.get_height()))

        pygame.display.update()

    # # every time loop, check for events that have occurred
    while run:
        clock.tick(FPS)  # monitors when to update physics

        redraw_window(finish=finished)

        if door_1.clicked == True and door_2.clicked == True and door_3.clicked == True:
            finished = True
            finished_count += 1

        if player.lives == 0:
            finished = True
            finished_count += 1

        if finished:
            # for more than 3 seconds
            if finished_count >= FPS * 3:
                run = False
            else:
                continue

        # # # looks at all events except keys
        for event in pygame.event.get():
            # # # if close window then end game and close window
            if event.type == pygame.QUIT:
                run = False

        # # # dictionary of keys pressed during the current frame; top left corner is always checked
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + velocity_x > 0:
            player.x -= velocity_x
        if keys[pygame.K_RIGHT] and player.x + velocity_x < WIDTH - player.img.get_width():
            player.x += velocity_x
        if keys[pygame.K_DOWN] and player.y + velocity_y <= HEIGHT - player.img.get_height() + velocity_y:
            player.y += velocity_y
        if keys[pygame.K_SPACE]:
            player.shoot()
