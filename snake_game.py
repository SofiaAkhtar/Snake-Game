import pygame
import sys
import random
import time

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10
GAME_OVER_WAIT_TIME = 2

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Directional constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT

    def move(self, food):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        if new_head == food.position:
            self.body.insert(0, food.position)
            food.spawn()
        else:
            self.body.insert(0, new_head)
            self.body.pop()

    def check_collision(self):
        head = self.body[0]
        return (
            head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT or
            head in self.body[1:]
        )

    def change_direction(self, new_direction):
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake()
        self.food = Food()
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)

    def main(self):
        while True:
            self.handle_events()

            self.snake.move(self.food)
            if self.snake.check_collision():
                self.game_over()

            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)

    def game_over(self):
        print("Game Over!")
        pygame.display.flip()
        time.sleep(GAME_OVER_WAIT_TIME)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.main()
