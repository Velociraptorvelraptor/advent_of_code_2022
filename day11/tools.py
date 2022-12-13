import math

class Monkey:
    """
    Represents single monkey with its features.
    """
    def __init__(self, number, items: list, operation_sign,
                 operation_value, divisible_by, if_true, if_false):
        self.number = number
        self.items = items
        self.operation_sing = operation_sign
        self.operation_value = operation_value
        self.divisble_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false
        self.monkey_business = 0

    def operation(self, if_mod=False, mod_value=0):
        old = self.items.pop(0)
        if self.operation_sing == '*':
            v = old * self.operation_value
        elif self.operation_sing == '+':
            v = old + self.operation_value
        elif self.operation_sing == '^':
            v = old ** 2
        return v % mod_value if if_mod == True else v

    def gets_bored(self, old):
        return math.floor(old / 3.)

    def check_if_divisible(self, old):
        if old % self.divisble_by == 0:
            return self.if_true
        else:
            return self.if_false


monkey_dict = dict()
monkey_dict[0] = Monkey(0, [64, 89, 65, 95], '*', 7, 3, 4, 1)
monkey_dict[1] = Monkey(1, [76, 66, 74, 87, 70, 56, 51, 66], '+', 5, 13, 7, 3)
monkey_dict[2] = Monkey(2, [91, 60, 63], '^', None, 2, 6, 5)
monkey_dict[3] = Monkey(3, [92, 61, 79, 97, 79], '+', 6, 11, 2, 6)
monkey_dict[4] = Monkey(4, [93, 54], '*', 11, 5, 1, 7)
monkey_dict[5] = Monkey(5, [60, 79, 92, 69, 88, 82, 70], '+', 8, 17, 4, 0)
monkey_dict[6] = Monkey(6, [64, 57, 73, 89, 55, 53], '+', 1, 19, 0, 5)
monkey_dict[7] = Monkey(7, [62], '+', 4, 7, 3, 2)