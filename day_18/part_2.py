from utils.solver import BaseSolver


class Solver(BaseSolver):

    def get_distances(self, start, end, corrupted, width=70, height=70):
        visited = set()
        distances = {start: 0}
        paths = {start: [start]}
        while end not in visited:
            current = None
            for node in distances:
                if node in visited:
                    continue
                if current is None or distances[node] < distances[current]:
                    current = node

            if current is None:
                return None, None

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
                    paths[new] = paths[current] + [new]

        return distances, paths

    def solve(self):
        data = self.read_input(row_wise=True, dtype=int, delimiter=",")
        corrupted = [(row[0], row[1]) for row in data]
        idx = 1024

        width = 70
        height = 70
        start = (0, 0)
        end = (width, height)

        _, paths = self.get_distances(
            start, end, corrupted[:idx], width=width, height=height
        )
        while idx < len(corrupted):
            # Could optimize with binary search
            pos = corrupted[idx]
            if pos in paths[end]:
                # Only need to rerun the pathfinding if the path is blocked
                _, paths = self.get_distances(
                    start, end, corrupted[: idx + 1], width=width, height=height
                )
                if paths is None:
                    return pos

            idx += 1

        assert False
