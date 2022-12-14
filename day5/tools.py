class SingleStack:
    """
    Represents single stack of crates.
    Provides methods to manipulate crates within the stacks.
    """
    def __init__(self, idx: int):
        self.idx = idx
        self.stack = []

    def add_to_stack(self, element: str):
        self.stack.append(element)

    def add_multiple_to_stack(self, list_of_elements: [str]):
        self.stack.extend(list_of_elements)

    def remove_from_stack(self) -> str:
        return self.stack.pop()

    def remove_multiple_from_stack(self, n: int) -> list[str]:
        popped_elements = []
        for _ in range(n):
            el = self.stack.pop()
            popped_elements.insert(0, el)
        return popped_elements

    def reverse_order(self):
        self.stack.reverse()


class StackManager():
    """
    Represents structure of stacks.
    """
    def __init__(self, n_stacks: int):
        self.stacks = {}
        self.n_stacks = n_stacks
        for i in range(self.n_stacks):
            self.stacks[i + 1] = SingleStack(i)

    def reverse_all_stacks(self):
        for i in range(self.n_stacks):
            self.stacks[i + 1].reverse_order()


def calculate_number_of_stacks(input: str) -> int:
    """
    Calculate numbers of stacks in the structure.
    :param input: string sequence with stacks visualization from the input file
    :return: number of stacks in the structure
    """
    n_stacks = []
    for line in input:
        n_stacks.append(len(line.split()))
    return max(n_stacks)