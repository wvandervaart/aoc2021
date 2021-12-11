def getInput(path):
    input = []
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def flash(grid, r, c):
    global f
    f[r][c] = 1
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i == r and j == c: continue
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                grid[i][j] += 1
                if grid[i][j] == 10:
                    flash(grid, i, j)
                    grid[i][j] += 1

def step(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
            if grid[r][c] == 10:
                flash(grid, r, c)
                grid[r][c] += 1
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] > 9:
                grid[r][c] = 0




def main():
    global f
    lines = getInput("input")
    grid = [list(map(int, line)) for line in lines]
    f = [[0] * len(r) for r in grid]
    s = 0 
    while True:
        s += 1
        step(grid)
        if all(map(all, f)):
            print(s)
            break
        f = [[0] * len(r) for r in grid]
    

if __name__ == "__main__":
    main()
