from utils.solver import BaseSolver


class Solver(BaseSolver):

    def get_shortest_path(self, start, end, track):
        width = len(track[0])
        height = len(track)
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
                if track[new[0]][new[1]] == "#":
                    continue
                distance = distances[current] + 1
                if new not in distances or distance < distances[new]:
                    distances[new] = distance

        return distances

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter="char")
        track = []
        check_pos = set()
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "S":
                    start = (i, j)
                if data[i][j] == "E":
                    end = (i, j)

                if data[i][j] != "#":
                    continue

                if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
                    continue

                adj_pos = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                adj_vals = [data[x][y] for x, y in adj_pos]
                empty = [".", "S", "E"]
                if adj_vals[0] in empty and adj_vals[1] in empty:
                    check_pos.add(((adj_pos[0]), (adj_pos[1])))
                    continue

                if adj_vals[2] in empty and adj_vals[3] in empty:
                    check_pos.add(((adj_pos[2]), (adj_pos[3])))
                    continue

            track.append(list(data[i]))

        cheats = 0
        cheat_map = {}
        distances = self.get_shortest_path(start, end, track)
        for i, pos in enumerate(check_pos):
            enter, exit = pos
            delta = abs(distances[exit] - distances[enter]) - 2
            if delta > 0:
                if delta not in cheat_map:
                    cheat_map[delta] = 0
                cheat_map[delta] += 1

            if delta >= 100:
                cheats += 1

        return cheats
