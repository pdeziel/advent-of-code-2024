from utils.solver import BaseSolver


class Solver(BaseSolver):

    def get_combo(self, registers, op):
        if op in [0, 1, 2, 3]:
            return op

        reg_map = {
            4: "A",
            5: "B",
            6: "C",
        }
        return registers[reg_map[op]]

    def solve(self):
        data = self.read_input(row_wise=True, dtype=str, delimiter="ws")
        registers = {}

        done_registers = False
        for row in data:
            if len(row) == 0:
                done_registers = True
                continue

            if not done_registers:
                registers[row[1][:-1]] = int(row[2])
            else:
                instructions = [int(op) for op in row[1].split(",")]

        pointer = 0
        out = []
        while pointer < len(instructions):
            if pointer + 1 >= len(instructions):
                break

            code = instructions[pointer]
            operand = instructions[pointer + 1]

            if code == 0:
                combo = self.get_combo(registers, operand)
                registers["A"] = registers["A"] // (2**combo)
            elif code == 1:
                registers["B"] = registers["B"] ^ operand
            elif code == 2:
                combo = self.get_combo(registers, operand)
                registers["B"] = combo % 8
            elif code == 3:
                if registers["A"] != 0:
                    pointer = operand
                    continue
            elif code == 4:
                registers["B"] = registers["B"] ^ registers["C"]
            elif code == 5:
                combo = self.get_combo(registers, operand)
                out.append(combo % 8)
            elif code == 6:
                combo = self.get_combo(registers, operand)
                registers["B"] = registers["A"] // (2**combo)
            elif code == 7:
                combo = self.get_combo(registers, operand)
                registers["C"] = registers["A"] // (2**combo)

            pointer += 2

        return ",".join([str(o) for o in out])
