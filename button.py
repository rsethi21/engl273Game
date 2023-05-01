import pygame

class Button:
  def __init__(self, x, y, image):
    self.image = image
    self.x = x
    self.y = y
    self.imageRect = image.get_rect()
    self.clicked = False
  
  def draw(self, WIN):
    pos = pygame.mouse.get_pos()
    
      
    
    WIN.blit(self.image, (self.imageRect.x, self.imageRect.y))
