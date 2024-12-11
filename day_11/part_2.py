from utils.solver import BaseSolver


class Solver(BaseSolver):

    def count_stones(self, stones, blinks):
        if blinks == 0:
            return len(stones)

        total = 0
        for stone in stones:
            if (stone, blinks) in self.seen:
                count = self.seen[(stone, blinks)]
            else:
                if stone == 0:
                    count = self.count_stones([1], blinks - 1)
                elif len(str(stone)) % 2 == 0:
                    str_val = str(stone)
                    split = len(str_val) // 2
                    count = self.count_stones(
                        [int(str_val[:split]), int(str_val[split:])], blinks - 1
                    )
                else:
                    count = self.count_stones([stone * 2024], blinks - 1)

                self.seen[(stone, blinks)] = count
            total += count
        return total

    def solve(self):
        stones = self.read_input(row_wise=True, dtype=int, delimiter="ws")[0]

        self.seen = {}
        blinks = 75
        return self.count_stones(stones, blinks)
