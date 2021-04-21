import numpy as np

class KnapsackSubproblem():
    """
    An example of a subproblem instance for Knapsack

    Feel free to use this, or make your own representation.
    Feel free to add any relevant helper methods as well.
    Feel free to modify this
    """

    def __init__(self, total_capacity, items):
        #total capacity in the knapsack
        self.total_capacity = total_capacity
        # the problem instance
        self.items = items
        self.partial_sol = []
        # subset of items with weight less than the remaining capacity
        self.valid_items = dict(items)
        self.removed = []
        self.curr_val = 0
        self.remaining_capacity = total_capacity


def get_instance(n, total_capacity, min_wt = 0, max_wt = None):
    """
    gets an instance of the knapsack problem.
    """
    max_wt = max_wt or 3*total_capacity/n
    vals = np.random.uniform(0,1, size=n)
    wts = np.random.uniform(min_wt,max_wt,size=n)
    items = {i:{'val':v,'wt':w} for i,v,w in enumerate(zip(vals,wts))}
    return items, total_capacity


class KnapsackBB():
    """
    Branch and bound implementation for the max Knapsack problem
    """

    def __init__(self):
        # add any instance variables
        pass

    def prune(self, subproblem, best_val) -> bool:
        """
        Return true if the current branch in the search tree
        can be pruned.

        Recall that the subproblem represents a node in an implicit
        search tree. This function should prune the tree at the node
        represented by the subproblem if no child of the current subproblem
        can yield a solution value larger than the best value.

        """
        if not self.legalQ(subproblem):
            return True

        if self.bound(subproblem) <= best_val:
            return True

        if self.completeQ(subproblem):
            return True

        return False

    def legalQ(self, subproblem) -> bool:
        """
        Return True iff the subproblem constitutes a legal solution
        """
        # TODO
        pass

    def completeQ(self, subproblem) -> bool:
        """
        Return True iff the subproblem cannot be extended - that is,
        the current knapsack can not be enlarged.
        """
        # TODO
        pass

    def bound(self, subproblem) -> float:
        """
        Bound the potential solution quality of the (implicit) subtree rooted
        at the current subproblem.

        Recall that the subproblem represents a node in an implicit
        search tree. In the case of knapsack, this function
        should return an upper bound on the maximum value of any (valid)
        subproblem in the subtree rooted at this node

        suggestion: consider the fractional knapsack solution value.
        """
        # TODO
        pass

    def get_solution_and_value(self, subproblem):
        """
        Given a subproblem, return (partial_solution, value) tuple.
        """
        pass
        # TODO

    def get_next_choice(self, subproblem):
        """
        Proposes a next choice (item) to include in the subproblem's partial
        solution.
        The choice of next item can be arbitrary, or it can depend in some way
        on the current subproblem.
        For example, when choosing the next item to consider, you could choose
        (1) an item not in the knapsack whose weight is less than the remaining capacity.
        (2) Among all such items, the item with the largest value.
        """
        # TODO
        pass

    def solve(self, items, capacity):
        # create an appropriate subproblem, and call the _solve method
        pass
        # TODO

    def _solve(self, subproblem, best_sol, best_val):
        # update the best solution and the best solution value
        partial_sol, partial_sol_val = self.get_solution_and_value(subproblem)
        if best_val < partial_sol_val:
            best_sol, best_val = partial_sol, partial_sol_val

        if self.prune(subproblem, best_val):
            return best_sol, best_val

        # if we made it here, then there is a possibility that a
        # better solution exists in this subtree

        # get the next choice (item) that should be added
        # to the subproblem's partial solution
        # TODO

        # i. generate a partial solution P' and subproblem
        # S' that includes the choice
        # TODO

        # recursively find the best solution with choice made
        # TODO

        # restore the subproblem back to it's state before the choice was made
        # TODO

        # recursively find best solution without choice made
        # TODO

        # restore the subproblem back to its original state (if appropriate)
        # TODO

        # compare the best solution values with and without the choice made and
        # return the better of the two
        # TODO

        return best_sol, best_val


class Knapsack:
    """
    Brute force implementation of Knapsack problem.

    Feel free to use subroutines from assignment1 here
    """

    def solve(self, items):
        # TODO
        pass

