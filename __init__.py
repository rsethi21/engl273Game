import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

pygame.init()

vec = pygame.math.Vector2
h = 300
w = 650
acceleration = 0.3
friction = -0.10
framesPS = 60
framesPSClock = pygame.time.Clock()
count = 0

displaysurface = pygame.display.set_mode((w, h))
pygame.display.set_caption("A Game Dedicated to Gothic Literature")
