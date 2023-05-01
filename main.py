# necessary imports
import pygame
import os
import sys
from objects import Player, Enemy, Power
import time
import random

pygame.font.init()

# create pygame window (where game will be played on)
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A game dedicated to gothic texts")

# load images (creates surfaces)
imgDir = "gameImages"
# # background images
bedroomImage = pygame.image.load(os.path.join(imgDir, "bedroom.jpg"))
bedroomImage = pygame.transform.scale(bedroomImage, (WIDTH, HEIGHT))

doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))

# # characters
dracula = pygame.image.load(os.path.join(imgDir, "dracula.png"))
dracula = pygame.transform.scale(dracula, (WIDTH / 4, HEIGHT / 1.8))

frankenstein = pygame.image.load(os.path.join(imgDir, "frankenstein.png"))
frankenstein = pygame.transform.scale(frankenstein, (WIDTH / 4, HEIGHT / 1.25))

# # powers
spawnBats = pygame.image.load(os.path.join(imgDir, "batspower.png"))
spawnBats = pygame.transform.scale(spawnBats, (dracula.get_width() * 2, dracula.get_height()))


# game loop function (allows interaction and changes in physics)

def main():
    run = True
    FPS = 60  # checks physics 60 frames per second
    lives = 5
    lost = False
    lost_count = 0
    velocity_y = 5  # higher velocity for lower clock-speed; how many pixels moved per frame
    velocity_x = 8
    power_velocity = -10
    main_font = pygame.font.SysFont("comicsans", 20)
    item_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 100)


    enemy = Enemy(WIDTH - dracula.get_width(), HEIGHT - dracula.get_height(), dracula)  # dummy character create
    enemy.powers = list([Power(spawnBats, "Spawn Bats", enemy.x, enemy.y)])

    enemy2 = Player(10, HEIGHT - frankenstein.get_height(), frankenstein)

    clock = pygame.time.Clock()  # keeps track of time of game

    # # want to do one-two things well in gaming inside function (might want different functions for different
    # choices and call in different conditionals in loop
    def redraw_window(loss):
        # # created background
        WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        # # created text
        lives_label = main_font.render(f"Lives Left: {lives}", True, (255, 0, 0))  # RGB format tuple
        intro_text = item_font.render("Pick a Door", True, (255, 250, 250))
        door_1 = item_font.render("1", True, (255, 250, 250))
        door_2 = item_font.render("2", True, (255, 250, 250))
        door_3 = item_font.render("3", True, (255, 250, 250))

        # # plotting text
        WIN.blit(lives_label, (0, 0))
        WIN.blit(intro_text, (0.5 * WIDTH - 0.5 * intro_text.get_width(), 0))
        WIN.blit(door_1, (240, 40))
        WIN.blit(door_2, (0.5 * WIDTH - 0.5 * door_2.get_width(), 40))  # attempt at programmatic sense
        WIN.blit(door_3, (740, 40))

        enemy.draw(WIN)  # dummy character draw everytime checking frames
        enemy2.draw(WIN)

        if loss:
            loss_label = lost_font.render("Game Over = (!", True, (255, 0, 0))
            WIN.blit(loss_label,
                     (0.5 * WIDTH - 0.5 * loss_label.get_width(), 0.5 * HEIGHT - 0.5 * loss_label.get_height()))

        pygame.display.update()

    # # every time loop, check for events that have occurred
    while run:
        clock.tick(FPS)  # monitors when to update physics

        redraw_window(loss=lost)

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            # for more than 3 seconds
            if lost_count >= FPS * 3:
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
        if keys[pygame.K_LEFT] and enemy.x + velocity_x > 0:
            enemy.x -= velocity_x
        if keys[pygame.K_RIGHT] and enemy.x + velocity_x < WIDTH - enemy.img.get_width():
            enemy.x += velocity_x
        if keys[pygame.K_DOWN] and enemy.y + velocity_y <= HEIGHT - enemy.img.get_height() + velocity_y:
            enemy.y += velocity_y
        if keys[pygame.K_UP] and enemy.y + velocity_y > HEIGHT - enemy.img.get_height() - velocity_y:
            enemy.y -= velocity_y
            # lives -= 1  # random test
        if keys[pygame.K_SPACE]:
            enemy.shoot()
        if enemy.currentpower is not None:
            enemy.movePower(power_velocity, WIDTH, enemy2)
