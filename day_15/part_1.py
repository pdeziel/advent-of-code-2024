from utils.solver import BaseSolver


class Solver(BaseSolver):

    def push_blocks(self, warehouse, pos, dir):
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if warehouse[next_pos[0]][next_pos[1]] == "#":
            return pos

        if warehouse[next_pos[0]][next_pos[1]] == ".":
            warehouse[next_pos[0]][next_pos[1]] = warehouse[pos[0]][pos[1]]
            warehouse[pos[0]][pos[1]] = "."
            return next_pos

        pushed_pos = self.push_blocks(warehouse, next_pos, dir)
        if next_pos != pushed_pos:
            warehouse[next_pos[0]][next_pos[1]] = warehouse[pos[0]][pos[1]]
            warehouse[pos[0]][pos[1]] = "."
            return next_pos

        return pos

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
                warehouse.append(row)
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
            else:
                dir = (0, 1)

            pos = self.push_blocks(warehouse, pos, dir)

        sum = 0
        for i in range(len(warehouse)):
            for j in range(len(warehouse[i])):
                if warehouse[i][j] == "O":
                    sum += 100 * i + j

        return sum
