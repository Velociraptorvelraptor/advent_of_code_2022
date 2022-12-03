# --- Day 3: Rucksack Reorganization ---
# One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately,
# that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.
#
# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments.
# The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
#
# The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors.
# Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
#
# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.
#
# For example, suppose you have the following list of contents from six rucksacks:
#
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr,
# while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL.
# The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p),
# 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
#
# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

score = []

with open('input.txt') as f:
    for rucksack in f:
        items = [x for x in rucksack][:-1]
        comparment_1 = items[:int(len(items) / 2)]
        comparment_2 = items[int(len(items) / 2):]
        print(rucksack)
        for x in comparment_1:
            if x in comparment_2:
                print(x)
                score.append(x)
                break

def convert_to_num(char):
    if char.isupper() == True:
        v = ord(char) - 38
    else:
        v = ord(char) - 96
    return v

print(f'The priority for all the items is: {sum([convert_to_num(x) for x in score])}.')



# # --------- Part Two ---------

items = []
score = []

def find_triplicates(list):
    some_dict = {}
    for x in list:
        if x not in some_dict:
            some_dict[x] = 1
        else:
            some_dict[x] += 1
        if any(v == 3 for v in some_dict.values()):
            print(some_dict)
            return x


with open('input.txt') as f:
    for n, rucksack in enumerate(f):
        items.extend(set([x for x in rucksack][:-1]))
        if (n + 1) % 3 == 0:
            print('New_group')
            print(items)
            v = find_triplicates(items)
            print(v)
            print(convert_to_num(v))
            score.append(v)
            items = []

print(f'The priority for all badges: {sum([convert_to_num(x) for x in score])}.')

