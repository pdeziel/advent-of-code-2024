from utils.solver import BaseSolver


class Solver(BaseSolver):
    def is_valid(self, total, target, ops):
        if len(ops) == 0:
            return total == target

        return self.is_valid(total + ops[0], target, ops[1:]) or self.is_valid(
            total * ops[0], target, ops[1:]
        )

    def solve(self):
        equations = self.read_input(row_wise=True, dtype=str)
        sum = 0
        for eq in equations:
            target = int(eq[0][:-1])
            operands = [int(op) for op in eq[1:]]
            if self.is_valid(operands[0], target, operands[1:]):
                sum += target
        return sum
