from utils.solver import BaseSolver


class Solver(BaseSolver):

    def count_possible(self, patterns, design):
        if len(design) == 0:
            return 1

        patterns = tuple(patterns)
        if (patterns, design) in self.seen:
            return self.seen[(patterns, design)]

        total = 0
        for pattern in patterns:
            if design.startswith(pattern):
                total += self.count_possible(patterns, design[len(pattern) :])

        self.seen[(patterns, design)] = total
        return total

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter=",")
        patterns = []
        designs = []
        done_pattens = False
        for row in data:
            if row[0] == "":
                done_pattens = True
                continue

            if not done_pattens:
                patterns = [p.strip() for p in row]
            else:
                designs.append(row[0])

        self.seen = {}
        count = 0
        num = 0
        for design in designs:
            num += 1
            count += self.count_possible(patterns, design)

        return count
