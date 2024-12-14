from utils.solver import BaseSolver


class Solver(BaseSolver):

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter="ws")
        robots = []
        for row in data:
            pos, vel = row[0].split("=")[1].split(","), row[1].split("=")[1].split(",")
            pos = [int(p) for p in pos]
            vel = [int(v) for v in vel]
            robots.append([pos, vel])

        width = 11
        height = 7
        width = 101
        height = 103
        seconds = 100
        quadrants = [0 for _ in range(4)]
        for robot in robots:
            pos, vel = robot
            pos[0] = (pos[0] + vel[0] * seconds) % width
            pos[1] = (pos[1] + vel[1] * seconds) % height

            if pos[0] == width // 2 or pos[1] == height // 2:
                continue

            if pos[0] < width // 2 and pos[1] < height // 2:
                quadrants[0] += 1
            elif pos[0] > width // 2 and pos[1] < height // 2:
                quadrants[1] += 1
            elif pos[0] < width // 2 and pos[1] > height // 2:
                quadrants[2] += 1
            else:
                quadrants[3] += 1
        product = 1
        for q in quadrants:
            product *= q
        return product
