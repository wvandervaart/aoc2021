## Code borrowed from: https://github.com/plan-x64/advent-of-code-2021/blob/main/advent/day7.py
import sys

def find_min_fuel(input, cost_fn):
    ordered_input = sorted(input)
    (min, max) = (ordered_input[0], ordered_input[-1])
    costs = [(maybe_min, cost_fn(maybe_min, ordered_input)) for maybe_min in range(min, max)]
    return sorted(costs, key = lambda x: x[1])[0]

def main():
    transform = lambda x: [int(day) for day in str(x).split(',')]
    path = "input"
    input = []
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            input.append(transform(line))
    input = next(iter(input))

    pt1_cost_fn = lambda x_min, xs: sum([abs(x - x_min) for x in xs])
    pt2_cost_fn = lambda x_min, xs: sum([(abs(x - x_min)**2+abs(x - x_min))//2 for x in xs])

    print("Part1: {}".format(find_min_fuel(input, pt1_cost_fn)))
    print("Part2: {}".format(find_min_fuel(input, pt2_cost_fn)))
    
if __name__ == "__main__":
    main()
