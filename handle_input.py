import pygame
import game_manager

from command import *

class HandleInput:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(HandleInput, cls).__new__(cls)
            cls.game_manager = game_manager.GameManager()

            cls.command_dictionary = {
                pygame.K_w: (0, -1),
                pygame.K_s: (0, 1),
                pygame.K_a: (-1, 0),
                pygame.K_d: (1, 0)
            }
            
        return cls.instance
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == game_manager.GameManager.QUIT_EVENT:
                return CommandQuitGame(self.game_manager)
            if event.type == pygame.KEYDOWN:
                direction = self.command_dictionary.get(event.key)
                return CommandChangeDirection(direction, self.game_manager.snake)