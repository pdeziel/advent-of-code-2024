from utils.solver import BaseSolver

class Solver(BaseSolver):
    def check_report(self, report):
        prev = report.pop(0)
        dir = None
        for v in report:
            if v == prev:
                return False
            diff = v > prev
            if dir is not None and dir != diff:
                return False
            dir = diff

            if abs(v - prev) > 3:
                return False
            prev = v
        return True

    def solve(self):
        reports = self.read_input(row_wise=True, dtype=int)
        num_safe = sum(int(self.check_report(report)) for report in reports)
        return num_safe