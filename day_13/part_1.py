import numpy as np

from utils.solver import BaseSolver


class Solver(BaseSolver):

    def is_integer(self, n, tolerance=1e-5):
        if abs(n - round(n)) < tolerance:
            return True
        return False

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter="ws")
        machines = []
        a = None
        b = None
        prize = None
        for row in data:
            if len(row) == 0:
                continue

            if a is None:
                a = [row[2].split("+")[1][:-1], row[3].split("+")[1]]
            elif b is None:
                b = [row[2].split("+")[1][:-1], row[3].split("+")[1]]
            else:
                prize = [row[1].split("=")[1][:-1], row[2].split("=")[1]]
                machines.append([a, b, prize])
                a = None
                b = None
                prize = None

        # A * dAx + B * dBx = Cx
        # A * dAy + B * dBy = Cy
        cost = 0
        a_cost = 3
        b_cost = 1
        for machine in machines:
            a = np.array(
                [
                    [float(machine[0][0]), float(machine[1][0])],
                    [float(machine[0][1]), float(machine[1][1])],
                ]
            )
            b = np.array([float(machine[2][0]), float(machine[2][1])])
            res = np.linalg.solve(a, b)
            if self.is_integer(res[0]) and self.is_integer(res[1]):
                cost += res[0] * a_cost + res[1] * b_cost

        return int(cost)
