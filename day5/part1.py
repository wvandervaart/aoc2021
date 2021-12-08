###
#
# x1,y1 -> x2,y2
#
#
#
path = "input"
def parseData(path):
  with open(path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
  liness = {}
  grid = {}
  highx = 0
  highy = 0
  i = 0
  for line in lines:
    a, b = line.split('->')
    x1,y1 = a.split(',')
    x2,y2 = b.split(',')
    if int(x1) > highx:
      highx = int(x1)
    if int(x2) > highx:
      highx = int(x2)
    if int(y1) > highy:
      highy = int(y1)
    if int(y2) > highy:
      highy = int(y2)
    liness[i] = [int(x1),int(y1),int(x2),int(y2)]
    i += 1
  j = 0
  while j <= highx:
    k = 0
    gridline = []
    while k <= highy:
      gridline.append(0)
      k += 1
    grid[j] = gridline
    j += 1
  return grid, liness

def plotLines(lines, grid):

  for key, line in lines.items():
    # check if x1 = x2 or y1 = y2
    if line[0] == line[2] or line[1] == line[3]:
      if line[0] > line[2]:
        realx = line[2]
        highx = line[0]
      else:
        realx = line[0]
        highx = line[2]
      if line[1] > line[3]:
        y = line[3]
        highy = line[1]
      else:
        y = line[1]
        highy = line[3]
      while y <= highy:
        x = realx
        while x <= highx:
          grid[y][x] += 1
          x += 1
        y += 1
  return grid
        


grid, lines = parseData(path)
grid = plotLines(lines, grid)
counter = 0 
for key, value in grid.items():
  for pos in value:
    if pos > 1:
      counter += 1

print("Final count: " + str(counter))
