import pygame
from backStory import story
import os
from button import Button

pygame.font.init()

# create pygame window (where game will be played on)
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A game dedicated to gothic texts")

def main_menu():
    FPS = 60
    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True

    # load images (creates surfaces)
    imgDir = "gameImages"
    # # background images
    homeScreen = pygame.image.load(os.path.join(imgDir, "BG.jpg"))
    homeScreen = pygame.transform.scale(homeScreen, (WIDTH, HEIGHT))


    # # play button
    play = pygame.image.load(os.path.join(imgDir, "play.png"))
    play = pygame.transform.scale(play, (WIDTH / 4, HEIGHT / 8))

    while run:
        clock.tick(FPS)
        WIN.blit(homeScreen, (0,0))
        title = title_font.render("Click play key to begin...", True, (255, 0, 0))
        WIN.blit(title, (0.5 * WIDTH - 0.5 * title.get_width(), 0.5 * HEIGHT - 0.5 * title.get_height()))

        button = Button(0.5 * WIDTH - 0.5 * play.get_width(), 0.5 * HEIGHT - 0.5 * play.get_height() + 75, play)
        button.draw(WIN, story)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

main_menu()