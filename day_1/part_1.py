from utils.solver import BaseSolver

class Solver(BaseSolver):
    def solve(self):
        cols = self.read_input(row_wise=False, dtype=int)
        sum = 0
        while len(cols[0]) > 0:
            min_a = min(cols[0])
            min_b = min(cols[1])
            sum += abs(min_a - min_b)
            cols[0].remove(min_a)
            cols[1].remove(min_b)
        return sum