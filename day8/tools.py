from functools import reduce

class Tree:
    """
    Represents single tree in a forest.
    """

    def __init__(self, x, y, height):
        """
        :param x: row coordinate of the tree instance
        :param y: col coordinate of the tree instance
        :param height: value read from the matrix using coordinates (x, y)
        """
        self.x = int(x)
        self.y = int(y)
        self.height = int(height)
        self.score = []
        print(f'Here comes new tree - x: {self.x}, y: {self.y}, height: {self.height}')

    def check_if_visible_by_edge(self, edges):
        if self.x in edges or self.y in edges:
            return True
        else:
            return


class ForestManager:
    """
    Forest handler which performs operations on the forest.
    """

    def __init__(self, forest):
        self.forest = forest
        self.tree_row = []
        self.tree_col = []

    def print_forest(self):
        return self.forest

    def calculate_visibility(self, edges):
        """
        Iterates over the forest to check the trees' visibility.
        :return: Number of visible trees.
        """
        for x, row in enumerate(self.forest):
            for y, height in enumerate(self.forest[x]):
                new_tree = Tree(x, y, height)
                if new_tree.check_if_visible_by_edge(edges):
                    self.n_visible_trees += 1
                else:
                    heights_left = set([int(v) for v in row[:y]])
                    heights_right = set([int(v) for v in row[y+1:]])
                    heights_up = set([int(row[y]) for row in self.forest[:x]])
                    heights_down = set([int(row[y]) for row in self.forest[x+1:]])
                    surrounding = [heights_left, heights_right, heights_up, heights_down]
                    print(surrounding)
                    for s in surrounding:
                        if all(new_tree.height > height for height in s) == True:
                            print('its visible')
                            self.n_visible_trees += 1
                            break

        return self.n_visible_trees


    def calculate_optimal_tree(self):
        """
        Calculates the score for the optimal tree - please check the task instructions.
        :return: Maximum tree score in the forest.
        """
        scores = []
        for x, row in enumerate(self.forest):
            for y, height in enumerate(self.forest[x]):
                new_tree = Tree(x, y, height)
                heights_left = [int(v) for v in row[:y]]
                heights_left.reverse()
                heights_right = [int(v) for v in row[y + 1:]]
                heights_up = [int(row[y]) for row in self.forest[:x]]
                heights_up.reverse()
                heights_down = [int(row[y]) for row in self.forest[x + 1:]]
                surrounding = [heights_left, heights_right, heights_up, heights_down]
                if not all(surrounding):
                    new_tree.score.append(0)
                else:
                    for line in surrounding:
                        counter = 0
                        for tree in line:
                            if new_tree.height > tree:
                                counter += 1
                            else:
                                counter += 1
                                break
                        new_tree.score.append(counter)
                scores.append(reduce((lambda x, y: x * y), new_tree.score))

        return max(scores)
