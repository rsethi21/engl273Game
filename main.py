# necessary imports
import pygame
import os
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
doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))
# # characters
dracula = pygame.image.load(os.path.join(imgDir, "dracula.png"))



# create character class that can be used for multiple things like enemy and player
class Character:

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.img = None
        self.powers = []
        self.turn = False

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 10)

# game loop function (allows interaction and changes in physics)

def main():
    run = True
    FPS = 120  # checks physics 60 frames per second
    lives = 5
    velocity = 10  # higher velocity for lower clockspeed; how many pixels moved per frame
    main_font = pygame.font.SysFont("comicsans", 20)
    item_font = pygame.font.SysFont("comicsans", 40)

    box = Character(700, 400)  # dummy character create

    clock = pygame.time.Clock()  # keeps track of time of game

    # # want to do one-two things well in gaming inside function (might want different functions for different
    # choices and call in different conditionals in loop
    def redraw_window():
        WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen

        # # created text
        lives_label = main_font.render(f"Lives Left: {lives}", True, (255, 0, 0))  # RGB format tuple
        intro_text = item_font.render("Pick a Door", True, (255, 250, 250))
        door_1 = item_font.render("1", True, (255, 250, 250))
        door_2 = item_font.render("2", True, (255, 250, 250))
        door_3 = item_font.render("3", True, (255, 250, 250))

        # # plotting text
        WIN.blit(lives_label, (0, 0))
        WIN.blit(intro_text, (0.5*WIDTH-0.5*intro_text.get_width(), 0))
        WIN.blit(door_1, (240, 40))
        WIN.blit(door_2, (0.5*WIDTH-0.5*door_2.get_width(), 40)) # attempt at programmatic sense
        WIN.blit(door_3, (740, 40))

        box.draw(WIN)  # dummy character draw

        pygame.display.update()

    # # every time loop, check for events that have occurred
    while run:
        clock.tick(FPS)  # monitors when to update physics
        redraw_window()

        for event in pygame.event.get():
            # # # if close window then end game and close window
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()  # dictionary of key presses and move in certain direction
            if keys[pygame.K_LEFT] and box.x + velocity > 0:
                box.x -= velocity
            if keys[pygame.K_RIGHT] and box.x + velocity < WIDTH:
                box.x += velocity
            if keys[pygame.K_DOWN] and box.y + velocity < HEIGHT:
                box.y += velocity
            if keys[pygame.K_UP] and box.y + velocity > 0:
                box.y -= velocity

main()