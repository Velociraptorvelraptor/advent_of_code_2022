from collections import defaultdict

THRESHOLD = 100000

data = open('input.txt').read()
lines = [x for x in data.split('\n')]

memory_dict = defaultdict(int)
path = []

for i, line in enumerate(lines):
    chars = line.strip().split()
    if chars[1] == 'cd':
        if chars[2] == '..':
            path.pop()
        else:
            path.append(chars[2])
    elif chars[1] == 'ls':
        continue
    else:
        try:
            v = int(chars[0])
            #print(path, v)
            for i in range(len(path)):
                memory_dict['/'.join(path[:i+1])] += v
        except:
            pass

memory_allocated = sum([x for x in memory_dict.values() if x < THRESHOLD])
memory_to_free = int((memory_dict['/'] + 3e7) - 7e7)

print(f'Minimal memory usage to rm in order to free space for the new system is: '
      f'{min([x for x in memory_dict.values() if x > memory_to_free])}')
