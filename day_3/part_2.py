import re

from utils.solver import BaseSolver


class Solver(BaseSolver):
    def solve(self):
        lines = self.read_input(row_wise=True, dtype=str, delimiter=None)
        sum = 0
        enabled = True
        for line in lines:
            matches = re.findall(
                r"(do\(\)|don't\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\)", line
            )
            for match in matches:
                if match[0] == "do()":
                    enabled = True
                elif match[0] == "don't()":
                    enabled = False
                elif enabled:
                    sum += int(match[1]) * int(match[2])
        return sum
