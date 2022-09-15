with open('input') as file:
  rows = [row.strip() for row in file]
  columns = range(0, len(rows[0]))
  epsilon = gamma = ''
  carbon = oxygen = rows.copy()


# part 1
for col in columns:
  count = [row[col] for row in rows].count
  if count('1') >= count('0'):
    epsilon += '1'
    gamma += '0'
  else:
    epsilon += '0'
    gamma += '1'
cons = int(epsilon, 2) * int(gamma, 2)
print('part 1: power consumption is {}'.format(cons))


# part 2
def calculate(array, reverse=False):
  for col in columns:
    if len(array) == 1: break
    count = [row[col] for row in array].count
    if reverse: value = '0' if count('1') >= count('0') else '1' 
    else: value = '1' if count('1') >= count('0') else '0'
    array = [row for row in array if row[col] == value]
  return int(array[0], 2)
cons = calculate(oxygen) * calculate(carbon, reverse=True)
print('part 2: life support rating is {}'.format(cons))
