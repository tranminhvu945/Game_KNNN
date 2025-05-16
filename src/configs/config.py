import pygame
import os 
from src.helpers.resource_path import resource_path

pygame.init() 

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

pygame.display.set_caption("Chiến tranh chống Mỹ")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

BACKGROUND = pygame.image.load(resource_path("assets/images/war_background.jpg"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Frames per second
FPS = 60

HERO_SPEED = 3
HERO_MAX_HP = 5
# HERO_MAX_HP = 1
HERO_RELOAD_TIME = 500
ENEMY_SPEED = 1.5
ENEMY_SHOOT_RANGE = 200
ENEMY_RELOAD_TIME = 2000
BULLET_SPEED = 7
EXPLOSION_DURATION = 300