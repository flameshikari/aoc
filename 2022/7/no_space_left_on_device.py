from re import match, sub


with open('input') as file:
  lines = []
  for row in file:
    lines.append(row.rstrip())


path = '/'
output = []
part_1 = 0
part_2 = []


for key, line in enumerate(lines):
    if '$' in line:
        if 'cd' in line:
            cd = line.split()[2]
            if cd == '..':
                path = sub('/\w+/$', '/', path)
            else:
                path += f'{cd}/'
        if 'ls' in line:
            step = 1
            while True:
                try:
                    target = lines[key + step]
                except:
                    target = lines[key]
                if match('^(dir|[0-9]).*', target):
                    line = lines[key + step].split()
                    data = line[0]
                    name = line[1] + '/' if data == 'dir' else line[1]
                    output.append({'path': path + name, 'data': data})
                    step += 1
                else:
                    break


used_space = sum([int(x['data']) for x in output if x['data'] != 'dir'])
free_space = 70000000 - used_space


for x in output:
    summary = 0
    if x['data'] == 'dir':
        basepath = x['path']
        for y in output:
            if y['data'] == 'dir':
                continue
            if match(fr'^{basepath}', y['path']):
                summary += int(y['data'])
        if summary < 100000:
            part_1 += summary
        if free_space + summary >= 30000000:
            part_2.append(summary)


print(f'part 1: the sum of the total sizes of those directories is {part_1}')
print(f'part 2: the total size of that directory is {sorted(part_2)[0]}')
