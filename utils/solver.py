class BaseSolver:
    def __init__(self, input_path):
        self.input_path = input_path

    def read_input(self, row_wise=False, dtype=str):
        data = []
        with open(self.input_path, 'r') as file:
            for line in file.readlines():
                row_values = [dtype(v) for v in line.strip().split()]
                if row_wise:
                    data.append(row_values)
                else:
                    for i, value in enumerate(row_values):
                        try:
                            data[i].append(value)
                        except IndexError:
                            data.append([value])

        return data
    
    def solve(self):
        raise NotImplementedError("solve method not implemented")