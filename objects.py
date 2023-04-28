import pygame

class Background(pygame.sprite.Sprite, main=True, office=False)
    def __init__(self):
        super().__init__()
        # top left corner
        self.bgY = 0
        self.bgX = 0
        # office image
        self.officeimage = pygame.image.load("./gameImages/emptyoffice.avif")
        self.homeimage = pygame.image.load("./gameImages/multipledoors.avif")
    def render(self):
        # perhaps add a conditional to customize background to different types
        if office == True:
            displaysurface.blit(self.officeimage, (self.bgX, self.bgY))
        if main == True:
            displaysurface.blit(self.homeimage, (self.bgX, self.bgY))
    
class Ground(pygame.sprite.Sprite)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./gameImages/ground.avif")
        self.rect = self.image.get_rect(center = (350, 350))

    def render(self):
        displaysurface.blit(self.image, (self.rect.X, self.rect.Y))

class Player(pygame.sprite.Sprite)
    def __init__(self):
        super().__init__()

class Enemy(pygame.sprite.Sprite)
    def __init__(self):
        super().__init__()
