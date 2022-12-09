instructions = [x.strip().split() for x in open('input.txt').readlines()]

class Node:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_one_step(self, dir):
        try:
            assert dir in ['R', 'L', 'U', 'D']
            if dir == 'R':
                self.x += 1
            elif dir == 'L':
                self.x -= 1
            elif dir == 'U':
                self.y += 1
            elif dir == 'D':
                self.y -= 1
        except AssertionError as e:
            print(f'{dir} is not a valid direction.')


def move_tail(head, tail):
    dr = head.x - tail.x  # it's difference withing one row
    dc = head.y - tail.y

    if abs(dr) <= 1 and abs(dc) <= 1:
        pass
    elif abs(dc) >= 2 and abs(dr) >= 2:
        if tail.x < head.x:
            tail.x = head.x - 1
        else:
            tail.x = head.x + 1
        if tail.y < head.y:
            tail.y = head.y - 1
        else:
            tail.y = head.y + 1
    elif abs(dr) >= 2:
        if tail.x < head.x:
            tail.x = head.x - 1
        else:
            tail.x = head.x + 1
        tail.y = head.y
    elif abs(dc) >= 2:
        if tail.y < head.y:
            tail.y = head.y - 1
        else:
            tail.y = head.y + 1
        tail.x = head.x

    return tail.x, tail.y