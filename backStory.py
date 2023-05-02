import pygame
import os
from button import Button
from dialogue import Speech
from objects import Player
from home import main
from endScene import finale

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
    title_font = pygame.font.SysFont("comicsans", 40)
    player = None

    # load images
    doorImage = pygame.image.load(os.path.join(imgDir, "doors.jpg"))
    doorImage = pygame.transform.scale(doorImage, (WIDTH, HEIGHT))
    butlerImage = pygame.image.load(os.path.join(imgDir, "butler.png"))
    butlerImage = pygame.transform.scale(butlerImage, (WIDTH/3, HEIGHT/1.5))
    nextImage = pygame.image.load(os.path.join(imgDir, "next.png"))
    nextImage = pygame.transform.scale(nextImage, (WIDTH / 5, HEIGHT / 9))

    choiceOne = pygame.image.load(os.path.join(imgDir, "choice1.png"))
    choiceOne = pygame.transform.scale(choiceOne, (WIDTH/4, HEIGHT/1.5))
    choiceTwo = pygame.image.load(os.path.join(imgDir, "choice2.png"))
    choiceTwo = pygame.transform.scale(choiceTwo, (WIDTH/5, HEIGHT/1.5))
    choiceThree = pygame.image.load(os.path.join(imgDir, "choice3.png"))
    choiceThree = pygame.transform.scale(choiceThree, (WIDTH/5, HEIGHT/1.5))
    choiceFour = pygame.image.load(os.path.join(imgDir, "choice4.png"))
    choiceFour = pygame.transform.scale(choiceFour, (WIDTH/5, HEIGHT/1.5))

    # dialogue
    index = 0
    first = Speech("Welcome to Castle Virtula detective! We need your services.")
    second = Speech("Monsters have infested the castle and you must fight them!")
    third = Speech("These creatures are deceptive and may say some untrue things.")
    fourth = Speech("... such as not to trust me!")
    fifth = Speech("Once you are weak enough...I mean successful,")
    sixth = Speech("you will be paid handsomely. Good luck! You'll need it")
    dialogueList = [first, second, third, fourth, fifth, sixth]

    # create necessary objects
    option2 = Button(0.5*WIDTH-choiceTwo.get_width(), HEIGHT-choiceTwo.get_height()+20, choiceTwo)
    option3 = Button(0.5*WIDTH, HEIGHT-choiceThree.get_height(), choiceThree)
    option1 = Button(option2.x-choiceTwo.get_width(), HEIGHT-choiceOne.get_height(), choiceOne)
    option4 = Button(option3.x+choiceThree.get_width(), HEIGHT-choiceFour.get_height()+20, choiceFour)
    nextButton = Button(WIDTH - nextImage.get_width(), 0, nextImage)

    player1 = Player(10, HEIGHT - option1.image.get_height(), option1.image)
    player2 = Player(10, HEIGHT - option2.image.get_height(), option2.image)
    player3 = Player(10, HEIGHT - option3.image.get_height(), option3.image)
    player4 = Player(10, HEIGHT - option4.image.get_height(), option4.image)


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
                nextButton.draw(WIN)

        elif index == len(dialogueList):
            # draw character buttons
            # call pick avatar to make player and call main
            # call end story

            WIN.blit(doorImage, (0, 0))  # pygame uses 0,0 as top left to add surface on screen

            intro_text = title_font.render("Pick an Avatar", True, (255, 250, 250))
            WIN.blit(intro_text, (0.5 * WIDTH - 0.5 * intro_text.get_width(), 0))

            if option1.clicked:
                index += 1
                player = player1
                main(WIN, player1)
            else:
                option1.draw(WIN)

            if option2.clicked:
                index += 1
                player = player2
                main(WIN, player2)
            else:
                option2.draw(WIN)

            if option3.clicked:
                index += 1
                player = player3
                main(WIN, player3)
            else:
                option3.draw(WIN)

            if option4.clicked:
                index += 1
                player = player4
                main(WIN, player4)
            else:
                option4.draw(WIN)

        else:
            finale(WIN, player)
            run = False

        pygame.display.update()