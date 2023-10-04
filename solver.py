from maze import Maze
from player import Player
import pygame
from random import choice

# init pygame and create a window
pygame.init()

WINDOW = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze Solver")

clock = pygame.time.Clock()
FRAMERATE = 15

# Load Maze and initialize Player
MAZE = Maze(filename='MazeSolver/maze.json')
PLAYER = Player(MAZE.get_start_tile())

PATH = []

def next_move():
    global PATH
    
    avail_moves = MAZE.get_moves_for_tile(PLAYER.row, PLAYER.col)

    if avail_moves:
        pref_move = choice(avail_moves)
        PATH.append(((PLAYER.row, PLAYER.col), pref_move))
        MAZE.move(PLAYER, pref_move)
        # print(pref_move)
    else:
        # move back 1 step
        pos, played_move = PATH.pop()
        MAZE.move_back(PLAYER, played_move)
        # print(played_move, 'back')

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

    if not MAZE.reached_finish(PLAYER):
        next_move()
    else:
        print('Path Found')
        break

# Wait for user to exit app
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