from utils.solver import BaseSolver


class Solver(BaseSolver):
    def get_words(self, grid, i, j, length=4):
        words = []
        if j <= len(grid[i]) - length:
            words.append([(i, j + k) for k in range(length)])
        if i <= len(grid) - length and j <= len(grid[i]) - length:
            words.append([(i + k, j + k) for k in range(length)])
        if i <= len(grid) - length:
            words.append([(i + k, j) for k in range(length)])
        if i <= len(grid) - length and j >= length - 1:
            words.append([(i + k, j - k) for k in range(length)])

        return words

    def solve(self):
        grid = self.read_input(row_wise=True, dtype=str, delimiter="char")
        targets = ["XMAS", "SAMX"]
        found = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                words = self.get_words(grid, i, j, length=len(targets[0]))
                for w in words:
                    text = "".join([grid[x][y] for x, y in w])
                    if text in targets:
                        found += 1
        return found
