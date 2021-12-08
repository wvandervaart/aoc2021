import sys

def parseData(values):
    outputs = []
    opl = {}
    i = 0
    for value in values:
        output = value[1].strip()
        opl[i] = []
        for b in output.split(' '):
            outputs.append(b)
            opl[i].append(b) 
        i += 1
    return outputs, opl

def convertDigit(digit):
    if digit == 'acedgfb':
        return 8
    if digit == 'dab':
        return 7
    if digit == 'cdfgeb':
        return 6
    if digit == 'cdfbe':
        return 5
    if digit == 'eafb':
        return 4
    if digit == 'fbcad':
        return 3
    if digit == 'gcdfa':
        return 2
    if digit == 'ab':
        return 1
    if digit == 'cefabd':
        return 9


def getAnswer(outputs):
    counter = 0
    for output in outputs:
        if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
            counter += 1
    return counter

def getAnswer2(opl):
    opc = []
    for key, value in opl.items():
        number = ''
        for part in value:
            print(part)
            number += str(convertDigit(part))
        opc.append(number)
    print(opc)
        

def main():
    transform = lambda x: [day for day in str(x).split('|')]
    path = "input"
    input = []
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            input.append(transform(line))
    #input = next(iter(input))
    outputs, opl = parseData(input)
    print(outputs)
    print("Part1: " + str(getAnswer(outputs)))
    print("Part2: " + str(getAnswer2(opl)))
    
if __name__ == "__main__":
    main()
