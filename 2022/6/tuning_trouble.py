with open('input') as file:
  sequence = ''
  for row in file:
    stream = row


def find(arg):
  for index in range(len(stream)):
    try:
      sequence = list(''.join([stream[index+n] for n in range(arg)]))
    except:
      pass
    if len(sequence) == len(set(sequence)):
      return(index+arg)


print(f'part 1: start-of-packet marker is detected at {find(4)}')
print(f'part 2: start-of-message marker is detected at {find(14)}')
