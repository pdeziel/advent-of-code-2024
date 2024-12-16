from utils.solver import BaseSolver


class Solver(BaseSolver):
    def solve(self):
        maze = self.read_input(row_wise=True, dtype=str, delimiter="char")
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "S":
                    start = (i, j)

        self.seen = {}

        dir = (0, 1)
        paths = [(start, dir, 0, set([start]))]
        min_cost = None
        best_tiles = set()
        while len(paths) > 0:
            pos, dir, cost, tiles = paths.pop(0)
            if maze[pos[0]][pos[1]] == "E":
                if min_cost is None or cost < min_cost:
                    min_cost = cost
                    best_tiles = tiles
                elif cost == min_cost:
                    best_tiles = best_tiles.union(tiles)
                continue

            if (pos, dir) in self.seen:
                if self.seen[(pos, dir)] < cost:
                    continue

            self.seen[(pos, dir)] = cost

            if maze[pos[0]][pos[1]] == "#":
                continue

            paths.append(
                (
                    (pos[0] + dir[0], pos[1] + dir[1]),
                    dir,
                    cost + 1,
                    tiles.union({(pos[0] + dir[0], pos[1] + dir[1])}),
                )
            )
            paths.append((pos, (dir[1], -dir[0]), cost + 1000, tiles))
            paths.append((pos, (-dir[1], dir[0]), cost + 1000, tiles))

        return len(best_tiles)
