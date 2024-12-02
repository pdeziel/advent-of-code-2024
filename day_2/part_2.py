from utils.solver import BaseSolver

class Solver(BaseSolver):
    def check_safe(self, report):
        prev = report[0]
        dir = None
        for v in report[1:]:
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

    def check_report(self, report):
        if self.check_safe(report):
            return True

        for i in range(len(report)):
            if self.check_safe(report[:i] + report[i+1:]):
                return True
            
        return False
        

    def solve(self):
        reports = self.read_input(row_wise=True, dtype=int)
        num_safe = sum(int(self.check_report(report)) for report in reports)
        return num_safe