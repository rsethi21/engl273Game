import pygame
import sys
import os

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            pass

    background.render()
    ground.render()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
