hor = 0
depth = 0
aim = 0 
with open("list", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    val = stripped_line.split()
    if val[0] == "forward":
      hor += int(val[1])
      depth += (int(val[1])*aim)
    if val[0] == "down":
      aim += int(val[1])
    if val[0] == "up":
      aim -= int(val[1])
    print("hor: " + str(hor) + " depth: " + str(depth) + " aim: " + str(aim))
  total = hor * depth
  print("Total: " + str(total))
