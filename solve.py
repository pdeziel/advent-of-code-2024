import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int, required=True)
    parser.add_argument('-p', '--part', type=int, required=True)
    parser.add_argument('-e', '--example', action='store_true')
    args = parser.parse_args()

    module = __import__(f'day_{args.day}.part_{args.part}', fromlist=[''])
    data_path = os.path.join(os.path.dirname(__file__), f'day_{args.day}', 'data', 'example.txt' if args.example else 'input.txt')
    solver = module.Solver(data_path)
    result = solver.solve()
    print(result)