# necessary imports
import pygame
import os
import time
import random

# create pygame window (where game will be played on)
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A game dedicated to gothic texts")

# load images (creates surfaces)
imgDir = "gameImages"
# # background images
bedroomImage = pygame.image.load(os.path.join(imgDir, "bedroom.jpg"))
doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))
# # characters
dracula = pygame.image.load(os.path.join(imgDir, "dracula.png"))


# game loop function (allows interaction and changes in physics)
def main():
    run = True
    FPS = 60  # checks physics 60 frames per second
    clock = pygame.time.Clock()  # keeps track of time of game

    # # want to do one-two things well in gaming inside function (might want different functions for different
    # choices and call in different conditionals in loop
    def redraw_window():
        WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        pygame.display.update()

    # # every time loop, check for events that have occurred
    while run:
        clock.tick(FPS)  # monitors when to update physics
        redraw_window()

        for event in pygame.event.get():
            # # # if close window then end game and close window
            if event.type == pygame.QUIT:
                run = False


main()