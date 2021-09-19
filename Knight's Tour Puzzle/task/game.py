# Write your code here
from numpy import full


class KnightRider:
    """Algorithmic solution of knights path thru all the fields on a chessboard"""

    # todo increase the number of dims of the chessboard 3d, 4d etc
    def __init__(self, rows=8, columns=8):
        self.field = full((rows, columns), fill_value='_', dtype=str, order='F')
        self.rows = rows
        self.columns = columns

    def print_field(self):
        print('', (2 * self.columns + 4) * '-')
        for i in range(self.rows):
            print(f'{self.rows - i}|', *self.field[i], '|', sep=' ')
        print('', (2 * self.columns + 4) * '-')
        print('   ', *(i + 1 for i in range(self.columns)))

    def get_start(self):
        starting_pos = input('Enter the knight\'s starting position: ').split()

        two_numbers = len(starting_pos) == 2
        all_digits = all(i.isdigit() for i in starting_pos)

        if not two_numbers or not all_digits:
            print('Invalid dimensions!')
            quit()

        is_inrange = int(float(starting_pos[0])) - 1 in range(self.columns) \
            and int(float(starting_pos[1])) - 1 in range(self.rows)

        if is_inrange:
            start_column, start_row = map(int, starting_pos)
            start_column -= 1
            start_row = self.rows - start_row
            self.field[start_row, start_column] = 'X'
        else:
            print('Invalid dimensions!')


if __name__ == '__main__':
    jezdec = KnightRider()
    jezdec.get_start()
    jezdec.print_field()
