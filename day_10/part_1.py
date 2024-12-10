from utils.solver import BaseSolver


class Solver(BaseSolver):

    def in_limits(self, pos, grid):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

    def get_next_steps(self, pos, grid):
        height = grid[pos[0]][pos[1]]
        next_steps = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        next_steps = [
            step
            for step in next_steps
            if self.in_limits(step, grid) and grid[step[0]][step[1]] == height + 1
        ]
        return next_steps

    def solve(self):
        grid = self.read_input(row_wise=True, dtype=int, delimiter="char")
        trailheads = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    trailheads.append((i, j))

        sum = 0
        for head in trailheads:
            terminals = set()
            steps = [head]
            while len(steps) > 0:
                next_steps = []
                for step in steps:
                    next = self.get_next_steps(step, grid)
                    for s in next:
                        if grid[s[0]][s[1]] == 9:
                            terminals.add(s)
                        else:
                            next_steps.append(s)

                steps = next_steps
            sum += len(terminals)
        return sum
