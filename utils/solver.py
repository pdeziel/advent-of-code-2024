class BaseSolver:
    def __init__(self, input_path):
        self.input_path = input_path

    def read_input(self, row_wise=False, dtype=str, delimiter="ws"):
        data = []
        with open(self.input_path, "r") as file:
            for line in file.readlines():
                line = line.strip()
                if delimiter is not None:
                    if delimiter == "char":
                        row_values = [dtype(v) for v in line]
                    else:
                        splits = (
                            line.split(delimiter) if delimiter != "ws" else line.split()
                        )
                        row_values = [dtype(v) for v in splits]
                else:
                    row_values = dtype(line)
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
