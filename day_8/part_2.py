from itertools import permutations

from utils.solver import BaseSolver


class Solver(BaseSolver):
    def in_limits(self, pos, grid):
        return (
            pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])
        )

    def get_nodes(self, a, b, grid):
        nodes = set()
        dir = (a[0] - b[0], a[1] - b[1])
        pos = a
        while self.in_limits(pos, grid):
            nodes.add(pos)
            pos = (pos[0] + dir[0], pos[1] + dir[1])

        pos = a
        while self.in_limits(pos, grid):
            nodes.add(pos)
            pos = (pos[0] - dir[0], pos[1] - dir[1])
        return nodes

    def solve(self):
        grid = self.read_input(row_wise=True, dtype=str, delimiter="char")
        ants = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val != ".":
                    if val in ants:
                        ants[val].add((i, j))
                    else:
                        ants[val] = {(i, j)}

        antinodes = set()
        for _, locs in ants.items():
            for a, b in permutations(locs, 2):
                for n in self.get_nodes(a, b, grid):
                    antinodes.add(n)

        return len(antinodes)
