class Board:
    '''
    The Board class represents the game board for Connect Four.
    '''
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.grid = [["." for _ in range(self.columns)] for _ in range(self.rows)]

    def display(self) -> None:
        '''
        Display the game board.
        '''
        for row in self.grid:
            print("|" + " ".join(row) + "|")
        print(" " + " ".join(map(str, range(1, self.columns + 1))))

    def drop_disc(self, column: int, disc: str):
        '''
        Drop a disc into the specified column.
        '''
        for row in reversed(self.grid):
            if row[column] == ".":
                row[column] = disc
                return self.grid.index(row), column
        return None

    def is_full(self) -> bool:
        '''
        Check if the board is full. If so, the game is a draw.
        '''
        return all(cell != "." for row in self.grid for cell in row)

    def check_winner(self, disc: str) -> bool:  
        '''
        Check if the specified disc has won the game by connecting four discs.
        '''
        # Check horizontal
        for row in self.grid:
            for col in range(self.columns - 3):
                if all(row[col + i] == disc for i in range(4)):
                    return True

        # Check vertical
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if all(self.grid[row + i][col] == disc for i in range(4)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i][col + i] == disc for i in range(4)):
                    return True

        # Check diagonal (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row - i][col + i] == disc for i in range(4)):
                    return True

        return False