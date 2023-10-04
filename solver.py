from maze import Maze
from player import Player
import pygame
from random import choice

# init pygame and create a window
pygame.init()

WINDOW = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze Solver")
WINDOW.fill((0, 0, 0))

clock = pygame.time.Clock()
FRAMERATE = 15

# Load Maze and initialize Player
MAZE = Maze(filename='MazeGenerator/maze.json')
PLAYER = Player(MAZE.get_start_tile())

PATH = []

# Maze Solver Logic
def next_move():
    global PATH
    
    avail_moves = MAZE.get_moves_for_tile(PLAYER.row, PLAYER.col)

    if avail_moves:
        pref_move = choice(avail_moves)
        PATH.append(((PLAYER.row, PLAYER.col), pref_move))
        MAZE.move(PLAYER, pref_move)
    else:
        # move back 1 step
        pos, played_move = PATH.pop()
        MAZE.move_back(PLAYER, played_move)

# Display UI
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # WINDOW.fill((0, 0, 0))
    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)

    if not MAZE.reached_finish(PLAYER):
        next_move()
    else:
        print('Path Found')
        break

# save screenshot of maze
print('Saving image of maze')
pygame.image.save(WINDOW, 'MazeSolver/maze-solved.png')

print('Saved \nClose the window to exit')

# Wait for user to exit app
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # WINDOW.fill((0, 0, 0))
    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)