from tile import Tile
from json import load


class Maze:
    def __init__(self, filename):
        # initalize / load maze from json file
        with open(filename) as file:
            maze = load(file)
        
        self.size = maze['size']
        self.start_tile = maze['start']
        self.end_tile = maze['end']
        self.tiles = [[None] * self.size[0] for i in range(self.size[1])]
        
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                data = maze['tiles'][i][j]
                self.tiles[i][j] = Tile(data)

        self.tiles[self.start_tile[0]][self.start_tile[1]].visited = True

    def show_maze(self, window):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.tiles[row][col].show_tile(window)

    def get_tile(self, row, col):
        return self.tiles[row][col]
    
    def get_start_tile(self):
        return self.tiles[self.start_tile[0]][self.start_tile[1]]
    
    def reached_finish(self, player):
        return player.row == self.end_tile[0] and player.col == self.end_tile[1]
    
    def get_moves_for_tile(self, row, col):
        tile = self.get_tile(row, col)
        moves = []

        if not tile.top and not self.tiles[row - 1][col].visited:
            moves.append('top')
        if not tile.bottom and not self.tiles[row + 1][col].visited:
            moves.append('bottom')
        if not tile.left and not self.tiles[row][col - 1].visited:
            moves.append('left')
        if not tile.right and not self.tiles[row][col + 1].visited:
            moves.append('right')
        
        moves = list(set(moves) - tile.exclude_moves)

        return moves
        
    def move(self, player, pref_move):
        curr_tile = self.get_tile(player.row, player.col)
        
        self.tiles[curr_tile.row][curr_tile.col].visited = True
        # self.tiles[curr_tile.row][curr_tile.col].color = (255, 255, 255)

        new_row = curr_tile.row
        new_col = curr_tile.col
        
        if pref_move == 'top':
            new_row -= 1

        elif pref_move == 'bottom':
            new_row += 1
        
        elif pref_move == 'left':
            new_col -= 1
        
        elif pref_move == 'right':
            new_col += 1

        player.set_player_to_tile(self.get_tile(new_row, new_col))
        # self.tiles[new_row][new_col].color = (255, 255, 255)
        self.tiles[new_row][new_col].visited = True

    def move_back(self, player, played_move):
        curr_tile = self.get_tile(player.row, player.col)
        
        self.tiles[curr_tile.row][curr_tile.col].visited = False
        # self.tiles[curr_tile.row][curr_tile.col].color = (0, 255, 0)

        new_row = curr_tile.row
        new_col = curr_tile.col
        
        if played_move == 'bottom':
            new_row -= 1

        elif played_move == 'top':
            new_row += 1
        
        elif played_move == 'right':
            new_col -= 1
        
        elif played_move == 'left':
            new_col += 1

        player.set_player_to_tile(self.get_tile(new_row, new_col))
        self.tiles[new_row][new_col].exclude_moves.add(played_move)     # Add move to exclude_moves as it is not correct move


    # def get_unvisited_tile(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if self.tiles[row][col].visited == False:
                    return self.tiles[row][col]
        return None
