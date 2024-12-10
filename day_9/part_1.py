from utils.solver import BaseSolver


class Solver(BaseSolver):
    def solve(self):
        with open(self.input_path, "r") as f:
            data = f.read().strip()

        filled = [int(char) for i, char in enumerate(data) if i % 2 == 0]
        empty = [int(char) for i, char in enumerate(data) if i % 2 == 1]
        idx = 0
        checksum = 0
        filled_id = 0
        to_fill_id = len(filled) - 1
        while filled_id < to_fill_id:
            for _ in range(filled[filled_id]):
                checksum += idx * filled_id
                idx += 1

            spaces = empty[filled_id]
            while spaces > 0:
                num_filled = min(spaces, filled[to_fill_id])
                for _ in range(num_filled):
                    checksum += idx * to_fill_id
                    idx += 1
                    spaces -= 1

                if num_filled < filled[to_fill_id]:
                    filled[to_fill_id] -= num_filled
                else:
                    to_fill_id -= 1

            filled_id += 1

        for _ in range(filled[to_fill_id]):
            checksum += idx * to_fill_id
            idx += 1
        return checksum
