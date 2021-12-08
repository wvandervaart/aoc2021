prev = 0
counter = 0
with open("list", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    if int(prev) < int(stripped_line):
      counter += 1
    prev = stripped_line
  print(counter)
