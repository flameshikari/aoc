from string import ascii_lowercase as ascii

with open('input') as file:
  rucksacks = []
  for row in file:
    rucksacks.append(row.rstrip())


alpha = ascii + ascii.upper()
sum_1 = 0
sum_2 = 0


for index, rucksack in enumerate(rucksacks):
  first_comp = rucksack[:len(rucksack)//2]
  second_comp = rucksack[len(rucksack)//2:]
  for item in first_comp:
    if item in second_comp:
      sum_1 += 1 + alpha.index(item)
      break
  if (index + 1) % 3 == 0:
    for item in rucksacks[index-2]:
      if item in rucksacks[index-1]:
        if item in rucksacks[index]:
          sum_2 += 1 + alpha.index(item)
          break


print(f'part 1: sum of priorities is {sum_1}')
print(f'part 2: sum of priorities is {sum_2}')
