class SingleStack:
    """
    Represents single stack of crates.
    Provides methods to manipulate crates within the stacks.
    """
    def __init__(self, idx: int) -> None:
        self.idx = idx
        self.stack = []

    def add_to_stack(self, element: str):
        self.stack.append(element)

    def remove_from_stack(self):
        return self.stack.pop()

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

    def reverse_all_stacks(self) -> None:
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