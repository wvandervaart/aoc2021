cur = {0 : '', 1 : '', 2 : ''}
prev = {0 : '', 1 : '', 2 : ''}
i = 0
j = -1
k = 0
counter = 0
with open("list", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    cur[i] = int(stripped_line)
    i += 1
    if i == 3:
      i = 0
    if k > 2: 
      prevt = prev[0] + prev[1] + prev[2]
      curt = cur[0] + cur[1] + cur[2]
      if curt > prevt:
        counter += 1
      print("prev:" + str(prev))
      print("cur: " + str(cur))
    k += 1
    prev[i] = int(stripped_line)
  print(counter)
