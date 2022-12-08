from tools import ForestManager

data = open('input.txt').read()
sdata = data.split('\n')

EDGES = [0, 98]

# Iterate over x, y in the forest structure
# initiate a Tree with each number
# check if x or y coordinates are FLENGTH of FHEIGHT - if so, mark it as visible
# else take tree coorrdinates row and column, make set out of
# it and check if any value from this set is equal or higher,
# if so the tree is not visible, otherwise it is visible

forest_manager = ForestManager(sdata)

print(f'Number of visible trees in the forest is: '
      f'{forest_manager.calculate_visibility(EDGES)}.')


print(f'Optimal score for a tree in the forest is: '
      f'{forest_manager.calculate_optimal_tree()}.')




