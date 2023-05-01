import pygame

class Button:
  def __init__(self, x, y, image, func):
    self.image = image
    self.x = x
    self.y = y
    self.imageRect = image.get_rect()
    self.clicked = False
    self.func = func
  
  def draw(self, WIN):
    
    WIN.blit(self.image, (self.imageRect.x, self.imageRect.y))
    
    pos = pygame.mouse.get_pos()
    if self.rectImage.collidepoint(pos):
      pygame.draw.rect(WIN, pygame.Color(255, 255, 255, 128), pygame.Rect(self.imageRect.x, self.imageRect.y, self.imageRect.get_width(), self.imageRect.get_height()))
      if pygame.mouseget_pressed()[0] and self.clicked == False:
        self.func()
        self.clicked = True
