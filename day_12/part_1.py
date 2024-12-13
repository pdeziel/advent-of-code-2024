from utils.solver import BaseSolver


class Solver(BaseSolver):

    def in_limits(self, pos, garden):
        return 0 <= pos[0] < len(garden) and 0 <= pos[1] < len(garden[0])

    def find_region(self, garden):
        for i in range(len(garden)):
            for j in range(len(garden[i])):
                if garden[i][j] is not None:
                    return i, j

    def get_next_positions(self, pos):
        next_positions = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        return next_positions

    def solve(self):
        garden = self.read_input(row_wise=True, dtype=str, delimiter="char")

        price = 0
        region = (0, 0)
        while region is not None:
            region_tag = garden[region[0]][region[1]]
            edges = set()
            inside = set()

            positions = [region]
            garden[region[0]][region[1]] = None
            inside.add(region)
            while len(positions) > 0:
                next_positions = []
                for pos in positions:
                    for next_pos in self.get_next_positions(pos):
                        if self.in_limits(next_pos, garden):
                            tag = garden[next_pos[0]][next_pos[1]]
                            if tag is None:
                                if next_pos not in inside:
                                    edges.add((pos, next_pos))
                                continue

                            if tag == region_tag:
                                if next_pos not in inside:
                                    next_positions.append(next_pos)
                                    inside.add(next_pos)
                                garden[next_pos[0]][next_pos[1]] = None
                            else:
                                edges.add((pos, next_pos))
                        else:
                            edges.add((pos, next_pos))
                positions = next_positions
            price += len(edges) * len(inside)
            region = self.find_region(garden)
        return price
