from utils.solver import BaseSolver


class Solver(BaseSolver):

    def get_grid(self, robots, width, height):
        grid = [["." for _ in range(width)] for _ in range(height)]
        for robot in robots:
            pos = robot
            val = grid[pos[1]][pos[0]]
            if val == ".":
                grid[pos[1]][pos[0]] = "1"
            else:
                grid[pos[1]][pos[0]] = str(int(val) + 1)
        return grid

    def print_robots(self, grid):
        for row in grid:
            print("".join(row))

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter="ws")
        robots = []
        for row in data:
            pos, vel = row[0].split("=")[1].split(","), row[1].split("=")[1].split(",")
            pos = [int(p) for p in pos]
            vel = [int(v) for v in vel]
            robots.append([pos, vel])

        width = 101
        height = 103
        seconds = 1
        skip_frames = 1
        while True:
            num_in_range = 0
            new_pos = []
            for robot in robots:
                pos, vel = robot
                new_x = (pos[0] + vel[0] * seconds) % width
                new_y = (pos[1] + vel[1] * seconds) % height
                new_pos.append([new_x, new_y])

                # Specific for my input, may be different?
                if new_x >= 54 and new_x <= 86 and new_y >= 46 and new_y <= 77:
                    num_in_range += 1

            if num_in_range > 150:
                return seconds

            seconds += skip_frames
