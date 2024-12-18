from utils.solver import BaseSolver


class Solver(BaseSolver):

    def get_distances(self, start, end, corrupted, width=70, height=70):
        visited = set()
        distances = {start: 0}
        while end not in visited:
            current = None
            for node in distances:
                if node in visited:
                    continue
                if current is None or distances[node] < distances[current]:
                    current = node

            if current is None:
                return None

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

    def solve(self):
        data = self.read_input(row_wise=True, dtype=int, delimiter=",")
        corrupted = [(row[0], row[1]) for row in data]

        width = 70
        height = 70
        start = (0, 0)
        end = (width, height)
        min_val = 1024
        max_val = len(corrupted) - 1
        while min_val < max_val:
            idx = (min_val + max_val) // 2
            distances = self.get_distances(
                start, end, corrupted[: idx + 1], width=width, height=height
            )
            if distances is None:
                max_val = idx
                continue
            else:
                min_val = idx + 1

        return corrupted[min_val]
