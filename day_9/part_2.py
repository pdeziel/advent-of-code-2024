from utils.solver import BaseSolver


class Solver(BaseSolver):
    def solve(self):
        with open(self.input_path, "r") as f:
            data = f.read().strip()

        blocks = []
        id = 0
        for i, char in enumerate(data):
            if i % 2 == 0:
                blocks.append((int(char), id))
                id += 1
            else:
                blocks.append((int(char), None))

        not_checked = [i for i in range(id)]
        last_idx = len(blocks) - 1
        while len(not_checked) > 0:
            idx = 0
            for i in range(last_idx, 0, -1):
                if blocks[i][1] in not_checked:
                    idx = i
                    break

            # Could be optimized by keeping better track of the blocks.
            # For example, keep track of the empty blocks so we don't have to forward
            # search for them.
            block = blocks[idx]
            for i in range(len(blocks)):
                if blocks[i][1] is None and idx > i:
                    size, file_id = blocks[i]
                    if block[0] <= size:
                        blocks[idx] = (block[0], None)
                        if block[0] < size:
                            blocks[i] = (size - block[0], file_id)
                            blocks.insert(i, block)
                        elif block[0] == size:
                            blocks[i] = block
                        break

            not_checked.remove(block[1])
            last_idx = idx

        checksum = 0
        idx = 0
        for i in range(len(blocks)):
            size, file_id = blocks[i]
            if file_id is not None:
                for _ in range(size):
                    checksum += idx * file_id
                    idx += 1
            else:
                idx += size

        return checksum
