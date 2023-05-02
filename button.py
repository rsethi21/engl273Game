import pygame


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.clicked = False
        self.cooldown = 0
        self.waitframes = 45

    def cool_down(self):
        if self.cooldown >= self.waitframes:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def draw(self, WIN, func=None, *args):

        pos = pygame.mouse.get_pos()
        if self.x <= pos[0] <= self.x + self.image.get_width() and self.y <= pos[1] <= self.y + self.image.get_height():

            img = self.image.copy()
            img.set_alpha(100)
            WIN.blit(img, (self.x, self.y))

            if pygame.mouse.get_pressed()[0] and self.clicked is False and self.cooldown == 0:
                if func != None:
                    func(WIN, *args)
                self.clicked = True
                self.cooldown = 1
        else:
            WIN.blit(self.image, (self.x, self.y))
