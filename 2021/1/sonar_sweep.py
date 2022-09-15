with open('input') as file:
  values = [int(num) for num in file]


# part 1
depth = 0
for i in range(0, len(values)-1):
  a = values[i]
  b = values[i+1]
  if b > a: depth += 1
print('part 1: {} measurments'.format(depth))


# part 2
depth = 0
for i in range(0, len(values)-3):
  a = values[i] + values[i+1] + values[i+2]
  b = values[i+1] + values[i+2] + values[i+3]
  if b > a: depth += 1
print('part 2: {} measurments'.format(depth))