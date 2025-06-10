import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.set_caption("Aim Trainer")  

TARGET_INCREMENT = "400"  
TARGET_EVENT = pygame.USER_EVENT  

TARGET_PADDING = 30

BG_COLOR = (0, 25, 40)
LIVES = 3
TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 22) 
