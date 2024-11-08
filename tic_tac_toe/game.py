class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def make_move(self, row, col, player):
        self.board[row][col] = player
    
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

# Создать игровое поле - объект класса Board.
game = Board()
# Отрисовать поле в терминале.
game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
game.make_move(1, 1, 'X')
print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
game.display() 