import string
from tools import StackManager, calculate_number_of_stacks

STACKS_FILENAME = 'input1.txt'
INSTRUCTIONS = 'input2.txt'

with open(STACKS_FILENAME) as f:
    input_lines = f.readlines()

n_stacks = calculate_number_of_stacks(input_lines)
input_col2stack_idx = {(i * 4 + 1): (i + 1) for i in range(n_stacks)}
stack_manager = StackManager(n_stacks)


for line in input_lines:
    for idx, element in enumerate(line):
        if element in string.ascii_letters:
            stack_idx = input_col2stack_idx[idx]
            stack_manager.stacks[stack_idx].add_to_stack(element)

stack_manager.reverse_all_stacks()

with open(INSTRUCTIONS) as f:
    instructions = f.readlines()

for line in instructions:
    line_elements = line.strip().split(' ')
    n = int(line_elements[1])
    origin = int(line_elements[3])
    destination = int(line_elements[5])
    block = stack_manager.stacks[origin].remove_multiple_from_stack(n)
    stack_manager.stacks[destination].add_multiple_to_stack(block)

output = ''.join([x.stack[-1] for x in stack_manager.stacks.values()])
print(f'Answer: {output}')
