with open('input') as file:
  rounds = []
  for row in file:
    rounds.append(row.split())


values = {'A': 1, 'X': 1,
          'B': 2, 'Y': 2,
          'C': 3, 'Z': 3}

win = ['AY', 'BZ', 'CX']
loss = ['AZ', 'BX', 'CY']

score_1 = 0
score_2 = 0


for round in rounds:
  you = round[1]
  foe = round[0]

  # part 1
  if foe + you in win:
    score_1 += 6 + values[you]
  elif foe + you in loss:
    score_1 += values[you]
  else:
    score_1 += 3 + values[you]

  # part 2
  if you == 'Z':
    for i in win:
      if i[0] == foe:
        score_2 += 6 + values[i[1]]
        break
  elif you == 'X':
    for i in loss:
      if i[0] == foe:
        score_2 += values[i[1]]
        break
  else:
    score_2 += 3 + values[foe]


print(f'part 1: your total score is {score_1}')
print(f'part 2: your total score is {score_2}')