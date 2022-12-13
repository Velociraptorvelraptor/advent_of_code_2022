from tools import monkey_dict

N_ROUNDS = 10000
MOD = 9699690

for _ in range(N_ROUNDS):
    for k, monkey in monkey_dict.items():
        for item in list(monkey.items):
            monkey.monkey_business += 1
            new_worry_value = monkey.operation(if_mod=True, mod_value=MOD)
            n = monkey.check_if_divisible(new_worry_value)
            monkey_dict[n].items.append(new_worry_value)

mb = []
for k, monkey in monkey_dict.items():
    mb.append(int(monkey.monkey_business))
mb.sort()