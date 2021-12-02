with open('input') as file:
  lines = []
  for line in file:
    line = line.split()
    lines += [[line[0], int(line[1])]]


# part 1
depth = pos = 0
for line in lines:
  cmd = line[0]; value = line[1]
  if cmd == 'down': depth += value
  elif cmd == 'up': depth -= value
  else: pos += value
print('part 1: {}'.format(depth*pos))


# part 2
aim = depth = pos = 0
for line in lines:
  cmd = line[0]; value = line[1]
  if cmd == 'down': aim += value
  elif cmd == 'up': aim -= value
  else:
    pos += value
    depth += value*aim
print('part 2: {}'.format(depth*pos))