import pygame
from game_manager import *

def main():
    pygame.init()
    game_manager = GameManager()
    game_manager.start()
    while game_manager.running == True:
        game_manager.handle_input()
        game_manager.update()
        game_manager.render()
    pygame.quit()    

main()