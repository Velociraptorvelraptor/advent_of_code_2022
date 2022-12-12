import numpy as np
from task1 import cycles, vdict

drawing = ''
crt_position = 1


for c in range(1, cycles):
    m = int((np.ceil(c / 40) - 1) * 40)
    print(f'New cycle has begun: {c - m}, crt position: {crt_position}, m: {m}')
    if c - m - 1 in [crt_position - 1, crt_position, crt_position + 1]:
        drawing += '#'
        print('Draw #')
    else:
        drawing += '.'
        print('Draw .')
    if c % 40 == 0:
        drawing += '\n'
        print('new line')
    crt_position += int(vdict[c])

    print(drawing)


# print(drawing)
# print(vdict)