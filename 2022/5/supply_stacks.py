from re import findall
from copy import deepcopy


with open('input') as file:
  procs = []
  crates = []
  crates_raw = []
  for row in file:
    tmp = []
    if 'move' in row:
      digits = [int(x) for x in findall(r'\b\d+\b', row)]
      procs.append(digits)
    if '[' in row:
      for col in range(1, len(row), 4):
        entry = row[col:col+1]
        tmp.append(entry)
      crates_raw.append(tmp)
  for col in range(len(crates_raw[0])):
    tmp = []
    for row in range(len(crates_raw)):
      char = crates_raw[row][col]
      if char.isalpha():
        tmp.append(char)
    crates.append(tmp[::-1])


def process(reverse=False):
  tmp = deepcopy(crates)
  for proc in procs:
    count = proc[0]
    src = proc[1]-1
    dst = proc[2]-1
    moving = tmp[src][-count:]
    for n in range(count):
      if len(tmp[src]) != 0:
        tmp[src].pop()
    if reverse: moving.reverse()
    tmp[dst] += moving
  return [crate[-1:][0] for crate in tmp]


print(f'part 1: tops of each stuck are {"".join(process(reverse=True))}')
print(f'part 2: tops of each stuck are {"".join(process(reverse=False))}')
