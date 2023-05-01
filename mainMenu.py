import pygame
from main import main
import os

# load images (creates surfaces)
imgDir = "gameImages"
# # background images
homeScreen = pygame.image.load(os.path.join(imgDir, "BG.jpg"))
homeScreen = pygame.transform.scale(homeScreen, (WIDTH, HEIGHT))

def main_menu(WIN):
    FPS = 60
    clock = pygame.time.Clock()
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    title_font = pygame.font.SysFont("comicsans", 50)
    button_font = pygame.font.SysFont("comicsans", 20)
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(homeScreen, (0,0))
        title = title_font.render("Click play key to begin...", True, (255, 0, 0))
        button = button_font.render("Play", True, (255, 255, 255))
        button_dimensions = (button.get_width(), button.get_height())
        WIN.blit(title, (0.5 * WIDTH - 0.5 * title.get_width(), 0.5 * HEIGHT - 0.5 * title.get_height()))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0.5 * WIDTH - 0.5 * button.get_width() <= mouse[0] <= 0.5 * WIDTH - 0.5 * button.get_width() + button_dimensions[0] and 0.5 * HEIGHT - 0.5 * button.get_height() + 40 <= mouse[1] <= 0.5 * HEIGHT - 0.5 * button.get_height() + 40 + button_dimensions[1]:
                    main()
        
        if 0.5 * WIDTH - 0.5 * button.get_width() <= mouse[0] <= 0.5 * WIDTH - 0.5 * button.get_width() + button_dimensions[0] and 0.5 * HEIGHT - 0.5 * button.get_height() + 40 <= mouse[1] <= 0.5 * HEIGHT - 0.5 * button.get_height() + 40 + button_dimensions[1]:
            pygame.draw.rect(WIN, (255, 75, 0), [0.5 * WIDTH - 0.5 * button.get_width(), 0.5 * HEIGHT - 0.5 * button.get_height() + 40, button_dimensions[0], button_dimensions[1]])
        else:
            pygame.draw.rect(WIN, (100, 75, 0), [0.5 * WIDTH - 0.5 * button.get_width(), 0.5 * HEIGHT - 0.5 * button.get_height() + 40, button_dimensions[0], button_dimensions[1]])
        WIN.blit(button, (0.5 * WIDTH - 0.5 * button.get_width(), 0.5 * HEIGHT - 0.5 * button.get_height() + 40))
        
        pygame.display.update()
    pygame.quit()
