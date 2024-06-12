import random


class GameOfLife:
    def __init__(self) -> None:
        self.grid = []
        self.rows = 5
        self.cols = 6

    def game_engine(self):
        self.make_grid()
        self.show_grid()
        self.update_grid()

    def make_grid(self):
        self.grid = [
            ['-', '-', '*', '-', '-', '-'],
            ['-', '-', '*', '-', '*', '-'],
            ['-', '*', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '*', '-'],
        ]

    def show_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print("-=" * 20)

    def count_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == '*':
                count += 1
        return count

    def update_grid(self):
        new_grid = [['-' for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)
                if self.grid[row][col] == '*' and (neighbors == 2 or neighbors == 3):
                    new_grid[row][col] = '*'
                elif self.grid[row][col] == '-' and neighbors == 3:
                    new_grid[row][col] = '*'
                else:
                    new_grid[row][col] = '-'
        self.grid = new_grid
        self.show_grid()


if __name__ == "__main__":
    game = GameOfLife()
    game.game_engine()
