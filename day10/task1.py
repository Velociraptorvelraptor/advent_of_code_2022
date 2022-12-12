from collections import defaultdict
import numpy as np

instructions = [x.strip().split() for x in open('input.txt').readlines()]

vdict = defaultdict(int)
vdict[0] = 1
cycles = 0
drawing = []

for i, signal in enumerate(instructions, 1):
    if signal[0] == 'noop':
        cycles += 1
    elif signal[0] == 'addx':
        cycles += 2
        v = signal[1]
        vdict[cycles] = v


def calculate_value(vdict, threshold):
    counter = 0
    for k, v in vdict.items():
        if k < threshold:
            counter += int(v)
    return counter * threshold


thresholds = [20, 60, 100, 140, 180, 220]
result = np.sum([calculate_value(vdict, x) for x in thresholds])
print(f'Answer: {result}')
