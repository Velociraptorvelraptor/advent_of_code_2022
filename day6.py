INPUT_FILE = 'input.txt'
N_DISTINCT = 4

with open(INPUT_FILE) as f:
    input = [x for x in f.readline()]

seq = input[:N_DISTINCT]

for i, char in enumerate(input[N_DISTINCT:], N_DISTINCT):
    if len(set(seq)) == N_DISTINCT:
        print(f'Answer: {i}, sequence: {seq}')
        break
    else:
        seq.pop(0)
        seq.extend(char)
