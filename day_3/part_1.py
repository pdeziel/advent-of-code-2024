import re

from utils.solver import BaseSolver


class Solver(BaseSolver):
    def solve(self):
        lines = self.read_input(row_wise=True, dtype=str, delimiter=None)
        sum = 0
        for line in lines:
            matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)
            for match in matches:
                sum += int(match[0]) * int(match[1])
        return sum
