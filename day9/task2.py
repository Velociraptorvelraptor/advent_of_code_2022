from tools import Node, move_tail, instructions

def follow_instructions(instructions):
    """
    :param instructions: Sequences of steps constructed of direction and n. of steps.
    :return: Set containing different tail coordinates (x, y).
    """
    head = Node()
    tail = [Node() for _ in range(9)]
    tail_positions = set()
    for dir, n_steps in instructions:
        n_steps = int(n_steps)
        for _ in range(n_steps):
            head.move_one_step(dir)
            tail[0].x, tail[0].y = move_tail(head, tail[0])
            for i in range(1, 9):
                tail[i].x, tail[i].y = move_tail(tail[i-1], tail[i])
            tail_positions.add((tail[8].x, tail[8].y))

    return tail_positions

print(f'Number of distinct tail coordinates (x, y) is:'
      f' {len(follow_instructions(instructions))}.')