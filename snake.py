from typing import Any
import pygame
from pygame import *
from pygame.sprite import *

import game_manager
from publisher import Publisher
from actor import Actor

class Snake(Actor, Publisher):
    # TODO: Doesn't feel right that I need to get scale and window_size through arguments. Should it be a static variable?
    def __init__(self, scale, window_size):
        Publisher.__init__(self)
        Actor.__init__(self, position=(40, 20), direction=(1, 0), size=16)

        self.length = 3
        self.scale = scale
        self.window_size = window_size

        # TODO: Decouple the events from GameManager?
        self.event = pygame.event.Event(game_manager.GameManager.QUIT_EVENT)
        self.body_group = Group()
        self.create_snake_body()

    def create_snake_body(self):
        for i in range (self.length):
            position = (self.position[0] - (self.direction[0] * i), self.position[1] - (self.direction[1] * i))
            SnakeSprite(self.scale, position, self.direction, self.size, self.body_group)  

    def add_to_snake_body(self):
        index = 0
        for body in self.body_group:
            if index == self.length - 1:
                position = (body.position[0] - body.direction[0], body.position[1] - body.direction[1])
                SnakeSprite(self.scale, position, self.direction, self.size, self.body_group)
        self.length += 1

    def update(self):
        self.move_snake()

        # Do Checks
        self.is_inside_window()
        self.is_on_self()

    # TODO: Confusing to read, needs to be cleaned somehow.
    def move_snake(self):
        index = 0
        for body in self.body_group:
            if index == 0:
                head_position = body.position
                body.position = (body.position[0] + body.direction[0], body.position[1] + body.direction[1])
                self.notify(head_position)
                
                head_direction = body.direction
            else:
                 aux_position = body.position
                 body.position = head_position
                 head_position = aux_position

                 aux_direction = body.direction
                 body.direction = head_direction
                 head_direction = aux_direction
            index += 1

    def change_direction(self, direction):
        index = 0
        for body in self.body_group:
                if index == 0:
                    body.direction = direction
                index += 1

    # TODO: I only need to perform checks on the head.
    def is_inside_window(self):
        for body in self.body_group:
            if body.position[0] not in range(self.window_size[0]) or body.position[1] not in range(self.window_size[1]):
                pygame.event.post(self.event)

    def is_on_self(self):
        index = 0
        for body in self.body_group:
            if index == 0:
                 head_position = body.position
            else:
                 if head_position == body.position:
                        pygame.event.post(self.event)
            index += 1

class SnakeSprite(Sprite):
    def __init__(self, scale, position, direction, size, group):
        Sprite.__init__(self, group)

        self.scale = scale
        self.size = size
        self.position = position
        self.direction = direction
        self.image = image.load("assets\\body.png")
        self.rect = pygame.Rect(self.scale * self.position[0], self.scale * self.position[1], self.size, self.size)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect = pygame.Rect(self.scale * self.position[0], self.scale * self.position[1], self.size, self.size)
        return super().update(*args, **kwargs)