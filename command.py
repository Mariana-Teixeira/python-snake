class Command():
    def execute(self):
        raise NotImplemented

class CommandChangeDirection(Command):
    def __init__(self, direction, snake):
        self.direction = direction
        self.snake = snake

    def execute(self):
        self.snake.change_direction(self.direction)

class CommandQuitGame(Command):
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def execute(self):
        self.game_manager.running = False