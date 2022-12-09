from tools import Node, move_tail, instructions

def follow_instructions(instructions):
    """
    :param instructions: Sequences of steps constructed of direction and n. of steps.
    :return: Set containing different tail coordinates (x, y).
    """
    head = Node()
    tail = Node()
    tail_positions = set()
    for dir, n_steps in instructions:
        n_steps = int(n_steps)
        tail_positions.add((tail.x, tail.y))
        for _ in range(n_steps):
            head.move_one_step(dir)
            tail.x, tail.y = move_tail(head, tail)
            tail_positions.add((tail.x, tail.y))

    return tail_positions

print(f'Number of distinct tail coordinates (x, y) is:'
      f' {len(follow_instructions(instructions))}.')