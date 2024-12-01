from utils.solver import BaseSolver

class Solver(BaseSolver):
    def solve(self):
        cols = self.read_input(row_wise=False, dtype=int)
        sim = 0
        for v in cols[0]:
            sim += v * sum(int(x == v) for x in cols[1])
        return sim