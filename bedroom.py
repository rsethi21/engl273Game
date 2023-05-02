import pygame
from button import Button
from dialogue import Speech
from objects import Enemy, Power
import os


def func1(WIN, player):
    pygame.font.init()

    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    run = True
    FPS = 60  # checks physics 60 frames per second
    finished = False
    finished_count = 0
    velocity_y = 5  # higher velocity for lower clock-speed; how many pixels moved per frame
    velocity_x = 8
    power_velocity = -10
    item_font = pygame.font.SysFont("comicsans", 40)
    end_font = pygame.font.SysFont("comicsans", 100)
    found = False

    # load images (creates surfaces)
    imgDir = "gameImages"
    # # background images
    bedroomImage = pygame.image.load(os.path.join(imgDir, "bedroom.jpg"))
    bedroomImage = pygame.transform.scale(bedroomImage, (WIDTH, HEIGHT))

    # # characters
    dracula = pygame.image.load(os.path.join(imgDir, "dracula.png"))
    dracula = pygame.transform.scale(dracula, (WIDTH / 4, HEIGHT / 1.8))

    # # powers
    spawnBats = pygame.image.load(os.path.join(imgDir, "batspower.png"))
    spawnBats = pygame.transform.scale(spawnBats, (dracula.get_width() * 2, dracula.get_height()))

    enemy = Enemy(WIDTH - dracula.get_width(), HEIGHT - dracula.get_height(), dracula)  # dummy character create
    enemy.powers = list([Power(spawnBats, "Spawn Bats", enemy.x, enemy.y)])

    clock = pygame.time.Clock()  # keeps track of time of game

    def redraw_window(finish, f):
        # # created background
        WIN.blit(bedroomImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        player.draw(WIN)

        if f is True:
            enemy.draw(WIN)  # dummy character draw everytime checking frames
        if player.x >= WIDTH * 0.5 and f is False:
            enemy.draw(WIN)
            f = True

        if finish:
            finished_label = end_font.render("You Lost =(!", True, (255, 0, 0))
            WIN.blit(finished_label,
                     (0.5 * WIDTH - 0.5 * finished_label.get_width(), 0.5 * HEIGHT - 0.5 * finished_label.get_height()))

        pygame.display.update()
        return f

    # # every time loop, check for events that have occurred
    while run:
        clock.tick(FPS)  # monitors when to update physics

        found = redraw_window(finished, found)

        if player.health <= 0:
            finished = True
            finished_count += 1

        if finished:
            # for more than 3 seconds
            if finished_count >= FPS * 3:
                player.health = 100
                player.lives -= 1
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
            enemy.shoot()
        if enemy.currentpower is not None:
            enemy.movePower(power_velocity, WIDTH, player)
        if player.currentpower is not None:
            player.movePower(power_velocity, WIDTH, enemy)
