import string

structure = {}

STACKS_FILENAME = 'input1.txt'
INSTRUCTIONS = 'input2.txt'

N_STACKS = 9
input_col2stack_idx = {(i * 4 + 1): (i + 1) for i in range(N_STACKS)}

with open(STACKS_FILENAME) as f:
    input_lines = f.readlines()

class SingleStack:
    def __init__(self, idx: int) -> None:
        self.idx = idx
        self.stack = []

    def add_to_stack(self, element: str):
        self.stack.append(element)

    def add_multiple_to_stack(self, list_of_elements: [str]):
        self.stack.extend(list_of_elements)

    def remove_from_stack(self):
        return self.stack.pop()

    def remove_multiple_from_stack(self, n: int):
        popped_elements = []
        for _ in range(n):
            el = self.stack.pop()
            popped_elements.insert(0, el)
        return popped_elements

    def reverse_order(self):
        self.stack.reverse()


class StackManager():
    def __init__(self, n_stacks: int):
        self.stacks = {}
        self.n_stacks = n_stacks
        for i in range(self.n_stacks):
            self.stacks[i + 1] = SingleStack(i)

    def reverse_all_stacks(self):
        for i in range(self.n_stacks):
            self.stacks[i + 1].reverse_order()

stack_manager = StackManager(N_STACKS)

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
    print(line_elements)
    block = stack_manager.stacks[origin].remove_multiple_from_stack(n)
    stack_manager.stacks[destination].add_multiple_to_stack(block)

output = [x.stack[-1] for x in stack_manager.stacks.values()]
print(''.join(output))