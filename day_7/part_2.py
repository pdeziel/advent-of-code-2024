from utils.solver import BaseSolver


class Solver(BaseSolver):
    def is_valid(self, total, target, ops):
        if total > target:
            return False

        if len(ops) == 0:
            return total == target

        if self.is_valid(total + ops[0], target, ops[1:]):
            return True

        if total != 0:
            if self.is_valid(total * ops[0], target, ops[1:]):
                return True

            if self.is_valid(int(str(total) + str(ops[0])), target, ops[1:]):
                return True

        return False

    def solve(self):
        equations = self.read_input(row_wise=True, dtype=str)
        sum = 0
        for eq in equations:
            target = int(eq[0][:-1])
            operands = [int(op) for op in eq[1:]]
            if self.is_valid(0, target, operands):
                sum += target
        return sum
