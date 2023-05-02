import pygame
from button import Button
from dialogue import Speech
from objects import Enemy, Power
import os


def func2(WIN, player):
    pygame.font.init()

    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    run = True
    FPS = 60  # checks physics 60 frames per second
    finished = False
    won = False
    finished_count = 0
    won_count = 0
    velocity_y = 5  # higher velocity for lower clock-speed; how many pixels moved per frame
    velocity_x = 8
    power_velocity = -10
    power_velocity_player = 10
    item_font = pygame.font.SysFont("comicsans", 20)
    end_font = pygame.font.SysFont("comicsans", 100)
    turn = True
    cooldownPlayer = 0
    cooldownEnemy = 0

    # load images (creates surfaces)
    imgDir = "gameImages"
    # # background images
    outdoorImage = pygame.image.load(os.path.join(imgDir, "outdoors.jpg"))
    outdoorImage = pygame.transform.scale(outdoorImage, (WIDTH, HEIGHT))

    # # characters
    frankenstein = pygame.image.load(os.path.join(imgDir, "frankenstein.png"))
    frankenstein = pygame.transform.scale(frankenstein, (WIDTH / 4, HEIGHT / 1.8))

    # # powers
    clouds = pygame.image.load(os.path.join(imgDir, "clouds.png"))
    clouds = pygame.transform.scale(clouds, (frankenstein.get_width() * 2, frankenstein.get_height()))

    superspeed = pygame.image.load(os.path.join(imgDir, "superspeed.png"))
    superspeed = pygame.transform.scale(superspeed, (frankenstein.get_width() * 2, frankenstein.get_height() * 0.5))

    insult = pygame.image.load(os.path.join(imgDir, "insult.png"))
    insult = pygame.transform.scale(insult, (player.img.get_width(), player.img.get_height() * 0.5))

    ignore = pygame.image.load(os.path.join(imgDir, "ignore.png"))
    ignore = pygame.transform.scale(ignore, (player.img.get_width(), player.img.get_height() * 0.5))

    # # move buttons and text

    moveButton = pygame.image.load(os.path.join(imgDir, "button.png"))
    moveButton = pygame.transform.scale(moveButton, (WIDTH / 4, HEIGHT / 8))

    moveButton1 = Button(moveButton.get_width(), HEIGHT - moveButton.get_height(), moveButton)
    moveButton2 = Button(moveButton.get_width() * 2 + 10, HEIGHT - moveButton.get_height(), moveButton)

    insultTitle = item_font.render("Insults", True, (255, 255, 255))

    ignoreTitle = item_font.render("Ignore", True, (255, 255, 255))

    enemy = Enemy(WIDTH - frankenstein.get_width(), HEIGHT - frankenstein.get_height(), frankenstein)  # dummy character create
    enemy.powers = list([Power(clouds, "Clouds", enemy.x, enemy.y, damage=35), Power(superspeed, "Super Speed", enemy.x, enemy.y)])
    player.powers = list(
        [Power(insult, "Insults", player.x, player.y, damage=20), Power(ignore, "Ignore", player.x, player.y, damage=20)])

    clock = pygame.time.Clock()  # keeps track of time of game

    def redraw_window(finish, w):
        # # created background
        WIN.blit(outdoorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        player.draw(WIN)
        enemy.draw(WIN)


    # # every time loop, check for events that have occurred
    while run:
        clock.tick(FPS)  # monitors when to update physics

        # # # looks at all events except keys
        redraw_window(finished, won)

        if player.health <= 0:
            finished = True
            finished_count += 1

        if enemy.health <= 0:
            won = True
            won_count += 1

        if finished:
            # for more than 3 seconds
            if finished_count >= FPS * 3:
                player.health = 100
                player.lives -= 1
                run = False
            else:
                finished_label = end_font.render("You Lost =(!", True, (255, 0, 0))
                WIN.blit(finished_label,
                         (0.5 * WIDTH - 0.5 * finished_label.get_width(),
                          0.5 * HEIGHT - 0.5 * finished_label.get_height()))

        if won:
            # for more than 3 seconds
            if won_count >= FPS * 3:
                player.health = 100
                run = False
            else:
                win_label = end_font.render("You Won =)!", True, (0, 0, 255))
                WIN.blit(win_label,
                         (0.5 * WIDTH - 0.5 * win_label.get_width(), 0.5 * HEIGHT - 0.5 * win_label.get_height()))


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

        if turn is False and cooldownEnemy <= 0:
            enemy.shoot()
            turn = True
            cooldownPlayer = FPS
        else:
            cooldownEnemy -= 1

        if turn is True and cooldownPlayer <= 0:

            if moveButton1.clicked:
                player.shoot(0)
                cooldownEnemy = FPS*2
                moveButton1 = Button(moveButton.get_width(), HEIGHT - moveButton.get_height(), moveButton)
                turn = False
            else:
                moveButton1.draw(WIN)
                WIN.blit(insultTitle, (moveButton1.x + 50, moveButton1.y + 15))

            if moveButton2.clicked:
                player.shoot(1)
                cooldownEnemy = FPS*2
                moveButton2 = Button(moveButton.get_width() * 2 + 10, HEIGHT - moveButton.get_height(), moveButton)
                turn = False
            else:
                moveButton2.draw(WIN)
                WIN.blit(ignoreTitle, (moveButton2.x + 50, moveButton2.y + 15))
        else:
            cooldownPlayer -= 1

        if enemy.currentpower is not None:
            enemy.movePower(power_velocity, WIDTH, player)

        if player.currentpower is not None:
            player.movePower(power_velocity_player, WIDTH, enemy)


        pygame.display.update()
