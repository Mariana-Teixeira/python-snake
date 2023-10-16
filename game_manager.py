import pygame
import handle_input
from snake import Snake
from food import Food
from publisher import Publisher

class GameManager:
    QUIT_EVENT = pygame.event.custom_type()
    ONFOOD_EVENT = pygame.event.custom_type()

    # TODO: Check Singleton implementation.
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(GameManager, cls).__new__(cls)
        return cls.instance

    def start(self):
        self.window_size = (80, 40)
        self.scale = 16

        self.running = True
        self.display = pygame.display.set_mode((self.scale * self.window_size[0], self.scale * self.window_size[1]))
        
        self.clock = pygame.time.Clock()
        self.input = handle_input.HandleInput()

        self.snake = Snake(self.scale, self.window_size)
        self.food = Food(self.scale, self.window_size)
        self.snake.add_observer(self.food)

    def handle_input(self):
        command = self.input.handle_input()
        if command != None:
            command.execute()

    def update(self):
        self.snake.update()

    def render(self):
        self.clock.tick(15)
        self.display.fill("white")

        self.snake.body_group.update()
        self.snake.body_group.draw(self.display)

        self.food.food_group.draw(self.display)
        pygame.display.flip()