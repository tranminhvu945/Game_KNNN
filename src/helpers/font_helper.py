import pygame
import os
from src.helpers.resource_path import resource_path

# Initialize font system
pygame.font.init()

# Font paths - adjust the filename to match your downloaded font
FONT_PATH = resource_path("assets/fonts/NotoSans-VariableFont_wdth,wght.ttf")
# Font sizes
FONT_LARGE = 70
FONT_MEDIUM = 45
FONT_SMALL = 36

_font_cache = {}

def get_font(size):
    """Get a font that supports Vietnamese at the specified size"""
    if size not in _font_cache:
        try:
            _font_cache[size] = pygame.font.Font(FONT_PATH, size)
        except FileNotFoundError:
            print(f"Warning: Font file {FONT_PATH} not found. Using system font.")
            _font_cache[size] = pygame.font.SysFont("Arial", size)
    return _font_cache[size]