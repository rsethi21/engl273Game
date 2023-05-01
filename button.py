import pygame


class Button:
    def __init__(self, x, y, image, func, *args):
        self.image = image
        self.x = x
        self.y = y
        self.clicked = False
        self.func = func
        self.args = args

    def draw(self, WIN):

        pos = pygame.mouse.get_pos()
        if self.x <= pos[0] <= self.x + self.image.get_width() and self.y <= pos[1] <= self.y + self.image.get_height():

            img = self.image.copy()
            img.set_alpha(100)
            WIN.blit(img, (self.x, self.y))

            if pygame.mouse.get_pressed()[0] and self.clicked is False:
                self.func(*self.args)
                self.clicked = True
        else:
            WIN.blit(self.image, (self.x, self.y))
