def getOxygen(values, bit, oxi):
  result = []
  bit = int(bit)
  zero = 0
  one = 0
  for value in values:
    if int(value[bit]) == 0:
      zero += 1
    if int(value[bit]) == 1:
      one += 1
  if zero == one:
    mostcommon = 1
    leastcommon = 0
  if zero > one:
    mostcommon = 0
    leastcommon = 1
  else:
    mostcommon = 1
    leastcommon = 0
  if oxi:
    check = mostcommon
  else:
    check = leastcommon
  for value in values:
    if str(value)[bit] == str(check):
      result.append(str(value))
  if len(result) == 1:
    return str(result[0])
  else:
    bit = bit + 1
    return getOxygen(result, bit, oxi)


values = []
result = [0,1,2,3,4,5,6,7,8,9,10,11]
result2 = [0,1,2,3,4,5,6,7,8,9,10,11]
#result = [0,1,2,3,4]
#result2 = [0,1,2,3,4]

with open("input", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    values.append(stripped_line)
  oxi = getOxygen(values, 0, True)
  co2 = getOxygen(values, 0, False)
  print("oxi: " + str(oxi) + " :: co2: " + str(co2))
  oxi = int(oxi, 2)
  co2 = int(co2, 2)
  print("oxi: " + str(oxi) + " :: co2: " + str(co2))
  print(oxi*co2)


    
    
