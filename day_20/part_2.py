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

    def get_cheats_adjusted(self, check_pos, dist, track):
        cheats = set()
        for i, pos in enumerate(check_pos):
            visited = set()
            queue = [(pos, 0)]
            while len(queue) > 0:
                current, depth = queue.pop(0)
                if depth > dist:
                    continue
                if current in visited:
                    continue
                if current[0] <= 0 or current[0] >= len(track) - 1:
                    continue
                if current[1] <= 0 or current[1] >= len(track[0]) - 1:
                    continue
                visited.add(current)
                if (
                    current != pos
                    and track[current[0]][current[1]] != "#"
                    and (current, pos) not in cheats
                ):
                    cheats.add((pos, current))
                for row, col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new = (current[0] + row, current[1] + col)
                    queue.append((new, depth + 1))

        return cheats

    def get_cheats(self, check_pos, dist, track):
        cheats = set()
        for i, pos in enumerate(check_pos):
            for i in range(-dist, dist + 1):
                for j in range(-dist, dist + 1):
                    new_pos = (pos[0] + i, pos[1] + j)
                    if new_pos[0] <= 0 or new_pos[0] >= len(track) - 1:
                        continue
                    if new_pos[1] <= 0 or new_pos[1] >= len(track[0]) - 1:
                        continue
                    if track[new_pos[0]][new_pos[1]] == "#":
                        continue
                    if (new_pos, pos) in cheats:
                        continue
                    cheats.add((pos, new_pos))

        return cheats

    def cart_dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

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
                    check_pos.add((i, j))

            track.append(list(data[i]))

        cheats = self.get_cheats_adjusted(check_pos, 20, track)
        total = 0
        cheat_map = {}
        distances = self.get_shortest_path(start, end, track)
        baseline_dist = distances[end]
        for i, pos in enumerate(cheats):
            enter, exit = pos
            delta = abs(distances[exit] - distances[enter]) - self.cart_dist(
                enter, exit
            )
            if delta >= 100:
                if delta not in cheat_map:
                    cheat_map[delta] = 0
                cheat_map[delta] += 1
                total += 1

        return total
