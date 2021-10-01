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
        self.row_marker = len(str(self.rows))
        # self.col_marker = len(str(self.columns))
        self.cell = len(str(self.columns * self.rows))
        self.field = np.chararray((self.rows, self.columns), itemsize=self.cell, order='F')
        self.field[:] = self.cell * '_'

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
            is_inrange = int(starting_pos[0]) - 1 in range(self.columns) and int(starting_pos[1]) - 1 in range(self.rows)

            if two_numbers and all_digits and is_inrange:
                start_column, start_row = map(int, starting_pos)
                start_column -= 1
                start_row = self.rows - start_row
                self.field[start_row, start_column] = (self.cell - 1) * ' ' + 'X'
                break
            else:
                print('Invalid position!')


if __name__ == '__main__':
    jezdec = KnightRider()
    jezdec.get_start()
    jezdec.print_field()

