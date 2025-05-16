from src.game import Game
import os
import sys
import pygame

def main():
    if sys.platform.startswith('win'):
        try:
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
        except:
            pass
    
    game = Game()
    game.run()

if __name__ == "__main__":
    main()