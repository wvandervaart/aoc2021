values = []
result = [0,1,2,3,4,5,6,7,8,9,10,11]
result2 = [0,1,2,3,4,5,6,7,8,9,10,11]
zero = 0
one = 0
with open("input", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    values.append(stripped_line)
    for i in range(0, 12):
      zero = 0
      one = 0
      for value in values:
        if int(value[i]) == 0:
          zero += 1
        if int(value[i]) == 1:
          one += 1
      if zero > one:
        result[i] = 0
        result2[i] = 1
      else:
        result[i] = 1
        result2[i] = 0
    print(result)
    print(result2)
  gamma = ''.join(map(str, result))
  epsilon = ''.join(map(str, result2))
  gamma = int(gamma, 2)
  epsilon = int(epsilon, 2)
  print(str(gamma) + ": " + str(epsilon))
  print(gamma*epsilon)
