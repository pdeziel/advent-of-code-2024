from itertools import permutations

from utils.solver import BaseSolver


class Solver(BaseSolver):
    def in_limits(self, pos, grid):
        return (
            pos[0] >= 0
            and pos[0] < len(grid)
            and pos[1] >= 0
            and pos[1] < len(grid[pos[0]])
        )

    def get_nodes(self, a, b):
        nodes = set()
        dir = (a[0] - b[0], a[1] - b[1])
        nodes.add((a[0] + dir[0], a[1] + dir[1]))
        nodes.add((b[0] + dir[0], b[1] + dir[1]))
        nodes.add((a[0] - dir[0], a[1] - dir[1]))
        nodes.add((b[0] - dir[0], b[1] - dir[1]))
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
                nodes = self.get_nodes(a, b)
                for n in nodes:
                    if n != a and n != b and self.in_limits(n, grid):
                        antinodes.add(n)

        return len(antinodes)
