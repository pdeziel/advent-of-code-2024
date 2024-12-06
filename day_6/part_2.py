from utils.solver import BaseSolver


class Solver(BaseSolver):
    def rot90(self, dir):
        if dir == (-1, 0):
            return (0, 1)
        if dir == (0, 1):
            return (1, 0)
        if dir == (1, 0):
            return (0, -1)
        if dir == (0, -1):
            return (-1, 0)
        assert False

    def get_path(self, lab, pos, dir):
        seen = set()
        dir = (-1, 0)

        while True:
            if (pos, dir) in seen:
                return None

            seen.add((pos, dir))
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if (
                next_pos[0] < 0
                or next_pos[0] >= len(lab)
                or next_pos[1] < 0
                or next_pos[1] >= len(lab[next_pos[0]])
            ):
                return seen

            if lab[next_pos[0]][next_pos[1]] == "#":
                dir = self.rot90(dir)
            else:
                pos = next_pos

    def solve(self):
        lab = self.read_input(row_wise=True, dtype=str, delimiter="char")
        for i in range(len(lab)):
            for j in range(len(lab[i])):
                if lab[i][j] == "^":
                    start = (i, j)
                    break

        path = self.get_path(lab, start, (-1, 0))
        found = set()
        for p in path:
            pos, _ = p
            lab[pos[0]][pos[1]] = "#"
            if self.get_path(lab, start, (-1, 0)) is None:
                found.add(pos)
            lab[pos[0]][pos[1]] = "."

        return len(found)
