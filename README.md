# Pygame Snake Game

This is a simple implementation of the classic Snake game using the Pygame library in Python. The game consists of a snake that moves around the screen, trying to eat food to grow longer. The objective is to survive as long as possible without colliding with the boundaries of the screen or the snake's own body.

## Prerequisites

Before running the game, make sure you have Python installed on your system. You will also need to install the Pygame library. You can do this by running the following command:

```bash
pip install pygame
```

## How to Run

To play the Snake game, execute the provided Python script:

```bash
python snake_game.py
```

## Controls

- Use the arrow keys (`UP`, `DOWN`, `LEFT`, `RIGHT`) to change the direction of the snake.

## Game Features

- The snake grows longer each time it consumes the red food.
- The game ends if the snake collides with the screen boundaries or itself.
- After a game over, the program waits for a few seconds before exiting.

## Constants

- `WIDTH` and `HEIGHT`: Dimensions of the game window.
- `GRID_SIZE`: Size of each grid cell.
- `FPS`: Frames per second for controlling the game speed.
- `GAME_OVER_WAIT_TIME`: Time to wait before exiting the game after a game over.

## Colors

- `WHITE`: RGB tuple representing the color white.
- `RED`: RGB tuple representing the color red.
- `GREEN`: RGB tuple representing the color green.
- `BLACK`: RGB tuple representing the color black.

## Classes

### Snake

- Represents the snake in the game.
- Methods include `move`, `check_collision`, `change_direction`, and `draw`.

### Food

- Represents the food that the snake can eat.
- Methods include `spawn` and `draw`.

### Game

- Initializes the Pygame environment and manages the game loop.
- Methods include `handle_events`, `main`, and `game_over`.

## Enjoy the game!
