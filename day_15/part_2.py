from utils.solver import BaseSolver


class Solver(BaseSolver):

    def get_moved(self, warehouse, pos, dir):
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if warehouse[next_pos[0]][next_pos[1]] == "#":
            return []

        if warehouse[next_pos[0]][next_pos[1]] == ".":
            return [pos]

        if dir == (0, 1) or dir == (0, -1):
            moved = self.get_moved(warehouse, next_pos, dir)
            if len(moved) == 0:
                return []
            return moved + [pos]
        else:
            if warehouse[next_pos[0]][next_pos[1]] == "[":
                next_left = next_pos
                next_right = (next_pos[0], next_pos[1] + 1)
            else:
                next_left = (next_pos[0], next_pos[1] - 1)
                next_right = next_pos

            moved_left = self.get_moved(warehouse, next_left, dir)
            moved_right = self.get_moved(warehouse, next_right, dir)
            if len(moved_left) == 0 or len(moved_right) == 0:
                return []
            return moved_left + moved_right + [pos]

    def print_warehouse(self, warehouse):
        for row in warehouse:
            print("".join(row))

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter="char")
        warehouse = []
        moves = []
        done_warehouse = False
        for row in data:
            if len(row) == 0:
                done_warehouse = True
                continue

            if not done_warehouse:
                str_row = (
                    "".join(row)
                    .replace("#", "##")
                    .replace("O", "[]")
                    .replace(".", "..")
                    .replace("@", "@.")
                )
                warehouse.append(list(str_row))
            else:
                moves.extend(row)

        for i in range(len(warehouse)):
            for j in range(len(warehouse[i])):
                if warehouse[i][j] == "@":
                    pos = (i, j)
                    break

        for move in moves:
            if move == "^":
                dir = (-1, 0)
            elif move == "v":
                dir = (1, 0)
            elif move == "<":
                dir = (0, -1)
            elif move == ">":
                dir = (0, 1)
            else:
                assert False

            moved = self.get_moved(warehouse, pos, dir)
            already_moved = set()
            for pos in moved:
                # Can't think of how to avoid duplication in recursion right now, so
                # just checking for duplicates here lol
                if pos in already_moved:
                    continue
                next_pos = (pos[0] + dir[0], pos[1] + dir[1])
                warehouse[next_pos[0]][next_pos[1]] = warehouse[pos[0]][pos[1]]
                warehouse[pos[0]][pos[1]] = "."
                already_moved.add(pos)
                pos = next_pos

        sum = 0
        for i in range(len(warehouse)):
            for j in range(len(warehouse[i])):
                if warehouse[i][j] == "[":
                    sum += 100 * i + j

        return sum
