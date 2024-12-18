from utils.solver import BaseSolver


class Solver(BaseSolver):

    def solve(self):
        data = self.read_input(row_wise=True, dtype=int, delimiter=",")
        corrupted = [(row[1], row[0]) for i, row in enumerate(data) if i < 1024]

        width = 70
        height = 70
        start = (0, 0)
        end = (width, height)

        visited = set()
        distances = {start: 0}
        while end not in visited:
            current = None
            for node in distances:
                if node in visited:
                    continue
                if current is None or distances[node] < distances[current]:
                    current = node

            visited.add(current)
            for row, col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new = (current[0] + row, current[1] + col)
                if new[0] < 0 or new[0] > width or new[1] < 0 or new[1] > height:
                    continue
                if new in visited:
                    continue
                if new in corrupted:
                    continue
                distance = distances[current] + 1
                if new not in distances or distance < distances[new]:
                    distances[new] = distance

        return distances[end]
