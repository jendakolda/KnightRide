# Write your code here
from numpy import chararray


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
        self.cell = len(str(self.columns * self.rows))
        self.field = chararray((self.rows, self.columns), itemsize=self.cell, order='F')
        self.field[:] = self.cell * '_'
        # print(self.field)
        # self.rows = rows
        # self.columns = columns

    def print_field(self):


        print(' ' + (self.columns*(self.cell + 1) + 3) * '-')
        for i in range(self.rows):
            prefix = len(str(self.rows)) - len(str(i))
            print(prefix)
            print(f'{(len(str(self.rows)) - len(str(i))) * " "} {self.rows - i}'|', *self.field[i].decode('utf-8'), '|', sep=' ')
        print('  ' + (self.columns*(self.cell + 1) + 3) * '-')
        print('  ', *(i + 1 for i in range(self.columns)))

    def get_start(self):
        starting_pos = input('Enter the knight\'s starting position: ').split()

        two_numbers = len(starting_pos) == 2
        all_digits = all(i.isdigit() for i in starting_pos)

        if not two_numbers or not all_digits:
            print('Invalid dimensions!')
            quit()

        is_inrange = int(starting_pos[0]) - 1 in range(self.columns) \
            and int(starting_pos[1]) - 1 in range(self.rows)

        if is_inrange:
            start_column, start_row = map(int, starting_pos)
            start_column -= 1
            start_row = self.rows - start_row
            self.field[start_row, start_column] = (self.cell - 1) * ' ' + 'X'
        else:
            print('Invalid position!')


if __name__ == '__main__':
    jezdec = KnightRider()
    jezdec.get_start()
    jezdec.print_field()

bytes()