import sys

def getLowPoints(values):
    points = []
    x = 0
    for value in values:
        y = 0
        for v in value:
            #print("check", "x", x, "y", y, "v", v)
            low = 0
            if x-1 != -1:
                if values[x-1][y] > v:
                    low += 1
            else:
                low += 1
            if x+1 < len(values):
                if values[x+1][y] > v:
                    low += 1
            else:
                low += 1
            if y-1 != -1:
                if values[x][y-1] > v:
                    low += 1
            else:
                low += 1
            if y+1 < len(value):
                if values[x][y+1] > v:
                    low += 1
            else:
                low += 1
            
            if low == 4:
                l = [x, y]
                points.append(l)
            y += 1
        x += 1
    return points

def compute_basins(inp, visited_nodes, o):
    if inp in visited_nodes:
        return []
    else:
        visited_nodes.append(inp)
    left_cords = []
    i_v = inp[1]
    j_v = inp [0]
    new_bto_iv = i_v
    while True:
        new_bto_iv -=  1
        if (new_bto_iv) < 0:
            break
        new_elm = o[j_v][new_bto_iv]
        if new_elm != 9:
            left_cords.append((j_v, new_bto_iv))
        else:
            break
    right_cords = []
    new_bto_il = i_v
    while True:
        new_bto_il +=  1
        if (new_bto_il) >= len(o[0]):
            break
        new_elm = o[j_v][new_bto_il]
        if new_elm != 9:
            right_cords.append((j_v, new_bto_il))
        else:
            break
    top_cords = []
    new_bto_jv = j_v
    while True:
        new_bto_jv -=  1
        if (new_bto_jv) < 0:
            break
        new_elm = o[new_bto_jv][i_v]
        if new_elm != 9:
            top_cords.append((new_bto_jv, i_v))
        else:
            break
    bot_cords = []
    new_bto_jb = j_v
    while True:
        new_bto_jb +=  1
        if (new_bto_jb) >= len(o):
            break
        new_elm = o[new_bto_jb][i_v]
        if new_elm != 9:
            bot_cords.append((new_bto_jb, i_v))
        else:
            break
    basin_cords = left_cords + right_cords + top_cords + bot_cords
    for cord in basin_cords:
        basin_cords += compute_basins(cord, visited_nodes, o)
    return list(set(basin_cords))




def getAnswer1(values, points):
    total = 0
    for point in points:
        total += int(values[point[0]][point[1]])+1
    return total


def main():
    path = "sample"
    #path = "input"
    input = []
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            input.append(list(line))
    points = getLowPoints(input)
    print("Part1:", getAnswer1(input, points))
    basin_sizes = []
    visited_nodes = []
    for point in points:
        basin_sizes.append(len(compute_basins(point, visited_nodes, input)))
        print(basin_sizes)
    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
    
if __name__ == "__main__":
    main()
