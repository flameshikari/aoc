with open('input') as file:
  count_1 = 0
  count_2 = 0
  for row in file:
    pairs = row.split()[0].split(',')
    pairs = [list(map(int, pair.split('-'))) for pair in pairs]
    left = list(range(pairs[0][0], pairs[0][1]+1))
    right = list(range(pairs[1][0], pairs[1][1]+1))
    if len(left) > len(right):
      if set(right).issubset(left):
        count_1 += 1
    else:
      if set(left).issubset(right):
        count_1 += 1
    if set(left) & set(right):
      count_2 += 1


print(f'part 1: {count_1} pairs fully contain one range in the other')
print(f'part 2: {count_2} pairs do the ranges overlap')
