import datetime

def getInput(path):
    input = []
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def unmatched(s):
    chars = list(s)
    openchars = ['[','(','{','<']
    closechars = [']',')','}','>']
    while 1:
        for i, c in enumerate(chars):
            if i+1 < len(chars):
                if c in openchars and chars[i+1] in closechars:
                    #print(c, chars[i+1])
                    if openchars.index(c) == closechars.index(chars[i+1]):
            #            print(i, i+1)
                        chars.pop(i+1)
                        chars.pop(i)
                        break
                    else:
                        return chars[i+1]
            else:
                return chars

def opened(s):
    chars = list(s)
    chars.reverse()
    openchars = ['[','(','{','<']
    closechars = [']',')','}','>']
    values = [2,1,3,4]
    points = 0
    for char in chars:
        points = points * 5
        points += values[openchars.index(char)]
    return points

def part1(chars):
    """
    
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.

    """
    points = 0
    for char in chars:
        if char == ')':
            points += 3
        if char == ']':
            points += 57
        if char == '}':
            points += 1197
        if char == '>':
            points += 25137
    return points

def part2(data):
    points = []
    for dat in data:
        points.append(opened(dat))
    points.sort()
    return points[len(points) // 2]


def main():
    begin_time = datetime.datetime.now()
    data = getInput("input")
    char = []
    incomplete = []
    for dat in data:
        char.append(unmatched(dat))
        if type(unmatched(dat)) == list:
            incomplete.append(unmatched(dat))
    print("P1:", part1(char))
    print("P2:", part2(incomplete))
    print("runtime:", datetime.datetime.now() - begin_time)

if __name__ == "__main__":
    main()
