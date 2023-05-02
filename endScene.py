import pygame
import os
from button import Button
from dialogue import Speech
from objects import Player


# basically create background and characters and list of text from NPC sequrntially released by user next button

def finale(WIN, player):
    # clock
    FPS = 60
    clock = pygame.time.Clock()
    finished = False

    # necessary variables
    run = True
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    imgDir = "gameImages"
    title_font = pygame.font.SysFont("comicsans", 100)

    # load images
    doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
    doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))
    butlerImage = pygame.image.load(os.path.join(imgDir, "butler.png"))
    butlerImage = pygame.transform.scale(butlerImage, (WIDTH / 3, HEIGHT / 1.5))
    nextImage = pygame.image.load(os.path.join(imgDir, "next.png"))
    nextImage = pygame.transform.scale(nextImage, (WIDTH / 5, HEIGHT / 9))

    # dialogue
    index = 0
    first = Speech("Hmm, unexpected.")
    second = Speech("I used those monsters to gain control over you and your gifts...")
    third = Speech("But, I guess I'll just have to do it myself!")
    dialogueList = [first, second, third]

    # create necessary objects
    nextButton = Button(WIDTH - nextImage.get_width(), 0, nextImage)


    while run:
        clock.tick(FPS)
        nextButton.cool_down()
        WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        WIN.blit(butlerImage, (WIDTH - butlerImage.get_width(), HEIGHT - butlerImage.get_height()))
        player.x = 10
        player.y = HEIGHT-player.img.get_height()
        player.draw(WIN)
        try:
            currentDialogue = dialogueList[index]
            currentDialogue.speech_bubble(WIN, (WIDTH - butlerImage.get_width(), HEIGHT - butlerImage.get_height()))
        except:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if 0 <= index <= len(dialogueList) - 1:
            if nextButton.clicked:
                index += 1
                nextButton.clicked = False
            else:
                nextButton.draw(WIN)

        else:
            run = False

        pygame.display.update()