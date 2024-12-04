from utils.solver import BaseSolver


class Solver(BaseSolver):
    def check_cross(self, grid, i, j):
        if grid[i][j] != "A":
            return False

        if i < 1 or j < 1:
            return False

        if i >= len(grid) - 1 or j >= len(grid[i]) - 1:
            return False

        illegal = ["A", "X"]
        top_left = grid[i - 1][j - 1]
        bottom_right = grid[i + 1][j + 1]
        if top_left in illegal or bottom_right in illegal:
            return False
        if top_left == bottom_right:
            return False

        top_right = grid[i - 1][j + 1]
        bottom_left = grid[i + 1][j - 1]
        if top_right in illegal or bottom_left in illegal:
            return False
        if top_right == bottom_left:
            return False

        return True

    def solve(self):
        grid = self.read_input(row_wise=True, dtype=str, delimiter="char")
        found = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if self.check_cross(grid, i, j):
                    found += 1

        return found
