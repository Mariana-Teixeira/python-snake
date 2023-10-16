from typing import Any
import pygame
from pygame import *
from pygame.sprite import *

import random
from observer import Observer
from actor import Actor

class Food(Actor, Observer):
    # TODO: Feels odd to pass window_size as an argument. Should it be a static variable?
    def __init__(self, scale, window_size):
        Actor.__init__(self, position=(50, 20), size= 16)
        self.scale = scale
        self.window_size = window_size

        self.food_group = GroupSingle()
        self.food = FoodSprite(self.scale, self.position, self.size, self.food_group)

    def get_new_position(self):
        position = (random.randrange(self.window_size[0]), random.randrange(self.window_size[1]))
        return position

    def on_notify(self, position):
        if self.position == position:
            self.position = self.get_new_position()            
            self.food.change_position(self.position)

class FoodSprite(Sprite):
    def __init__(self, scale, position, size, group):
        Sprite.__init__(self, group)
        self.scale = scale
        self.position = position
        self.size = size
        self.image = pygame.image.load("assets\\apple.png")
        self.rect = pygame.Rect(self.scale * self.position[0], self.scale * self.position[1], self.size, self.size)

    def change_position(self, position):
        self.position = position
        self.rect = pygame.Rect(self.scale * self.position[0], self.scale * self.position[1], self.size, self.size)