# Write your code here
import numpy as np


class KnightRider:
    """Algorithmic solution of knights path thru all the fields on a chessboard"""

    # todo increase the number of dims of the chessboard 3d, 4d etc
    def __init__(self, rows=8, columns=8):
        while True:
            board_dim = input('Enter your board dimensions: ').split()
            two_numbers = len(board_dim) == 2
            pos_digits = all(i.isdigit() and int(i) > 0 for i in board_dim)
            if two_numbers and pos_digits:
                self.columns, self.rows = map(int, board_dim)
                break
            else:
                print('Invalid dimensions!')
        self.row_marker = len(str(self.rows))
        self.cell = len(str(self.columns * self.rows))
        self.field = np.chararray((self.rows, self.columns), itemsize=self.cell, order='F')
        self.field[:] = self.cell * '_'
        self.current_column = None
        self.current_row = None

    def mark_cell(self, row, column, sign):
        self.field[row, column] = (self.cell - 1) * ' ' + sign

    def range_check(self, checked_row, checked_column):
        return checked_row in range(self.rows) and checked_column in range(self.columns)

    def print_field(self):
        print(self.row_marker * ' ' + (self.columns * (self.cell + 1) + 3) * '-')
        for i in range(self.rows):
            prefix = self.row_marker - len(str(self.rows - i))
            print(prefix * ' ' + f'{self.rows - i}|', *self.field[i].decode('utf-8'), '|', sep=' ')
        print(self.row_marker * ' ' + (self.columns * (self.cell + 1) + 3) * '-')
        numbers_below = (self.row_marker + 1) * ' '
        for i in range(self.columns):
            numbers_below += (self.cell - len(str(i + 1))) * ' ' + ' ' + str(i + 1)
        print(numbers_below)

    def get_start(self):
        while True:
            starting_pos = input('Enter the knight\'s starting position: ').split()
            two_numbers = len(starting_pos) == 2
            all_digits = all(i.isdigit() for i in starting_pos)

            if not two_numbers or not all_digits:
                print('Invalid position!')
            elif self.range_check(int(starting_pos[1]) - 1, int(starting_pos[0]) - 1):
                self.current_column, self.current_row = map(int, starting_pos)
                self.current_column -= 1
                self.current_row = self.rows - self.current_row
                self.mark_cell(self.current_row, self.current_column, 'X')
                self.field[self.current_row, self.current_column] = (self.cell - 1) * ' ' + 'X'
                break
            else:
                print('Invalid position!')

    def get_possible_moves(self):
        moves = ((- 1, -2,), (-2, -1), (1, -2), (-2, 1), (-1, 2), (2, -1), (1, 2), (2, 1))
        # possible_moves = []
        for move in moves:
            new_pos = (self.current_row + move[0], self.current_column + move[1])
            if self.range_check(new_pos[0], new_pos[1]):
                self.mark_cell(new_pos[0], new_pos[1], 'O')
                # possible_moves.append(new_pos)


if __name__ == '__main__':
    jezdec = KnightRider()
    jezdec.get_start()
    jezdec.get_possible_moves()
    jezdec.print_field()

