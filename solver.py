from maze import Maze
from player import Player
import pygame

# init pygame and create a window
pygame.init()

WINDOW = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze Solver")

clock = pygame.time.Clock()
FRAMERATE = 15

# Load Maze and initialize Player
MAZE = Maze(filename='maze.json')
PLAYER = Player(MAZE.get_start_tile())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    WINDOW.fill((0, 255, 0))
    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)