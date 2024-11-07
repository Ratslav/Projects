class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def make_move(self, row, col, player):
        self.board[row][col] = player
    print('sss')