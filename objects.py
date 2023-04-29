import pygame
import random


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x - obj1.img.get_width()/2
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None  # overlap based on offset?


# create character class that can be used for multiple things like enemy and player
class Character:

    def __init__(self, x, y, img, powerList=None, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.powers = powerList
        self.currentpower = None
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.shield = 3
        self.dodge = 3

    def draw(self, window):
        # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 10)  # test object
        window.blit(self.img, (self.x, self.y))
        self.healthbar(window)
        if self.currentpower is not None:
            self.currentpower.drawIt(window)

    def healthbar(self, window):
        percentHealth = self.health/self.max_health
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + 4, self.img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + 4, self.img.get_width() * percentHealth, 10))
class Player(Character):
    def __int__(self, x, y, img, powerList=None, health=100):
        super().__init__(x, y, img, powerList=powerList, health=health)
        # self.mask = pygame.mask.from_surface(self.img)


class Enemy(Character):
    def __init__(self, x, y, img, powerList=None, health=100):
        super().__init__(x, y, img, powerList=powerList, health=health)
        # self.mask = pygame.mask.from_surface(self.img)  # creates mask to create collisions perfect since only pixel
        # # areas

    def shoot(self):
        p = self.powers[random.randint(0, len(self.powers) - 1)]
        p.x = self.x
        p.y = self.y
        self.currentpower = p

    def movePower(self, vel_x, width, obj):
        self.currentpower.move(vel_x)
        if self.currentpower.off_screen(width):
            self.currentpower = None
        elif self.currentpower.collision(obj):
            obj.health -= self.currentpower.damage
            self.currentpower = None


class Power:
    def __init__(self, img, name, x, y, damage=10):
        self.x = x
        self.y = y
        self.img = img
        self.name = name  # give out description when used
        self.mask = pygame.mask.from_surface(self.img)
        self.damage = damage

    def drawIt(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel_x):
        self.x += vel_x

    def off_screen(self, width):
        return not (self.x <= width or self.x >= 0)

    def collision(self, obj):
        return collide(self, obj)  # does power intersect with character
