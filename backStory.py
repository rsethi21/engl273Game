import pygame
import os
from button import Button
from dialogue import Speech
from objects import Player
from home import main

# basically create background and characters and list of text from NPC sequrntially released by user next button

def story(WIN):

    # clock
    FPS = 60
    clock = pygame.time.Clock()

    # necessary variables
    run = True
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    imgDir = "gameImages"

    # load images
    doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
    doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))
    butlerImage = pygame.image.load(os.path.join(imgDir, "butler.png"))
    butlerImage = pygame.transform.scale(butlerImage, (WIDTH/3, HEIGHT/1.5))
    nextImage = pygame.image.load(os.path.join(imgDir, "next.png"))
    nextImage = pygame.transform.scale(nextImage, (WIDTH / 4, HEIGHT / 8))

    choiceOne = pygame.image.load(os.path.join(imgDir, "choice1.png"))
    choiceOne = pygame.transform.scale(choiceOne, (WIDTH / 4, HEIGHT / 2))
    choiceTwo = pygame.image.load(os.path.join(imgDir, "choice2.png"))
    choiceTwo = pygame.transform.scale(choiceTwo, (WIDTH / 4, HEIGHT / 2))
    choiceThree = pygame.image.load(os.path.join(imgDir, "choice3.png"))
    choiceThree = pygame.transform.scale(choiceThree, (WIDTH / 4, HEIGHT / 2))
    choiceFour = pygame.image.load(os.path.join(imgDir, "choice4.png"))
    choiceFour = pygame.transform.scale(choiceFour, (WIDTH / 4, HEIGHT / 2))

    # dialogue
    index = 0
    first = Speech("Welcome to Castle Virtula detective! We are in dire need of your services.")
    second = Speech("Monsters have infested the castle and we need your gifts to hunt these monsters down!")
    third = Speech("You must be careful though, as these creatures are deceptive and may say some untrue things, such as not to trust me!")
    fourth = Speech("Once inside, you must fight all the monsters in order to escape!")
    fifth = Speech("Once you are weak enoug...hehe...I mean successful, you will be paid handsomely. Good luck! You'll need it")
    dialogueList = [first, second, third, fourth, fifth]

    # create necessary objects
    option2 = Button(0.5*WIDTH-choiceTwo.get_width(), HEIGHT-choiceTwo.get_height(), choiceTwo)
    option3 = Button(0.5*WIDTH, HEIGHT-choiceThree.get_height(), choiceThree)
    option1 = Button(option2.x-choiceOne.get_width(), HEIGHT-choiceOne.get_height(), choiceOne)
    option4 = Button(option3.x+choiceThree.get_width(), HEIGHT-choiceFour.get_height(), choiceFour)
    nextButton = Button(WIDTH - nextImage.get_width(), HEIGHT - nextImage.get_height(), nextImage)

    # dummy function for button to work; may need to change in the future
    def redraw_window(window, speechIndex, pos):
        print(speechIndex)
        return

    def pick_avatar(window, x, y, img):
        # display pick and avatar text
        # create player object
        # call main function
        return


    while run:
        clock.tick(FPS)
        nextButton.cool_down()
        WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen
        WIN.blit(butlerImage, (WIDTH - butlerImage.get_width(), HEIGHT - butlerImage.get_height()))
        try:
            currentDialogue = dialogueList[index]
            currentDialogue.speech_bubble(WIN, (WIDTH - butlerImage.get_width(), HEIGHT - butlerImage.get_height()))
        except:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if 0 <= index <= len(dialogueList)-1:
            if nextButton.clicked:
                index += 1
                nextButton.clicked = False
            else:
                nextButton.draw(WIN, redraw_window, index, (WIDTH - butlerImage.get_width(), HEIGHT - butlerImage.get_height()))

        elif index == len(dialogueList):
            # draw character buttons
            # call pick avatar to make player and call main
            # call end story
            run = False

        pygame.display.update()