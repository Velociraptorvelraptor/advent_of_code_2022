from tools import monkey_dict

N_ROUNDS = 20

for _ in range(N_ROUNDS):
    for k, monkey in monkey_dict.items():
        for item in list(monkey.items):
            monkey.monkey_business += 1
            new_worry_value = monkey.operation(if_mod=False)
            new_worry_value = monkey.gets_bored(new_worry_value)
            n = monkey.check_if_divisible(new_worry_value)
            monkey_dict[n].items.append(new_worry_value)

    for k, monkey in monkey_dict.items():
        print(monkey.monkey_business)