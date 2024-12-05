from utils.solver import BaseSolver


class Solver(BaseSolver):
    def read_manual(self):
        rules = []
        updates = []

        with open(self.input_path, "r") as f:
            lines = f.readlines()
            read_rules = True
            for line in lines:
                if line.strip() == "":
                    read_rules = False
                    continue

                if read_rules:
                    rule = [int(v) for v in line.split("|")]
                    rules.append(rule)
                else:
                    update = [int(v) for v in line.split(",")]
                    updates.append(update)

        return rules, updates

    def is_valid(self, befores, afters, update):
        for i, page in enumerate(update):
            must_before = befores.get(page, set())
            must_after = afters.get(page, set())

            for req in must_before:
                if req in update and update.index(req) < i:
                    return False

            for req in must_after:
                if req in update and update.index(req) > i:
                    return False
        return True

    def solve(self):
        rules, updates = self.read_manual()
        befores = {}
        afters = {}
        for r in rules:
            before = r[0]
            after = r[1]

            if before not in befores:
                befores[before] = set([after])
            else:
                befores[before].add(after)

            if after not in afters:
                afters[after] = set([before])
            else:
                afters[after].add(before)

        sum = 0
        for update in updates:
            if self.is_valid(befores, afters, update):
                sum += update[int(len(update) / 2)]
        return sum
