# Write your code here
from numpy import empty, where


class KnightRider:
    """Algorithmic solution of knights path thru all the fields on a chessboard"""
    # todo increase the number of dims of the chessboard 3d, 4d etc
    def __init__(self, rows=8, columns=8):
        self.field = empty((rows, columns), dtype=str, order='F')
        self.rows = rows
        self.columns = columns

    def print_field(self):
        print((2 * self.columns + 2) * '-')
        for i in range(self.rows):
            print(f'{self.rows - i}|', *self.field[i], '|', sep=' ')
        print((2 * self.columns + 2) * '-')

    def get_start(self):
        starting_pos = input('Input the x & y coordinate of the starting position: ').split()
        is_valid = len(starting_pos) == 2 and all(i.isdigit() for i in starting_pos)
        is_inrange = int(starting_pos[0]) - 1 in range(self.columns) and int(starting_pos[1]) - 1 in range(self.rows)
        if is_valid and is_inrange:
            start_column, start_row = map(int, starting_pos)
            start_column -= 1
            start_row = self.rows - start_row


            print(start_column, start_row)
        else:
            print('Invalid dimensions!')



if __name__ == '__main__':
    jezdec = KnightRider()
    jezdec.get_start()
    jezdec.print_field()

