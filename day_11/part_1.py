from utils.solver import BaseSolver


class Solver(BaseSolver):

    def solve(self):
        stones = self.read_input(row_wise=True, dtype=int, delimiter="ws")[0]

        blinks = 25
        while blinks > 0:
            new_stones = []
            for stone in stones:
                if stone == 0:
                    new_stones.append(1)
                elif len(str(stone)) % 2 == 0:
                    str_val = str(stone)
                    split = len(str_val) // 2
                    new_stones.append(int(str_val[:split]))
                    new_stones.append(int(str_val[split:]))
                else:
                    new_stones.append(stone * 2024)
            stones = new_stones
            blinks -= 1

        return len(stones)
