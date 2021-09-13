# Write your code here
from numpy import empty, where


class KnightRider:
    def __init__(self, rows=8, columns=8):
        self.field = empty((rows, columns), dtype=str, order='F')
        self.rows = rows
        self.columns = columns

    def print_field(self):
        print((2 * self.columns + 2) * '-')
        for i in range(self.rows):
            print('|', *self.field[i], '|', sep=' ')
        print((2 * self.columns + 2) * '-')


if __name__ == '__main__':
    jezdec = KnightRider()
    jezdec.print_field()

