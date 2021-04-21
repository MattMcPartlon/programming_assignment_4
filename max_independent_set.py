import networkx


class IndependentSetSubproblem():
    """
    An example of a subproblem instance for Max Independent Set

    Feel free to use this, or make your own representation.
    Feel free to add any relevant helper methods as well.
    Feel free to modify this
    """

    def __init__(self, G):
        # The graph
        self.G = G
        # the current independent set
        self.partial_sol = []
        #subset of vertices not adjacent to any vertex in the partial solution
        self.non_nbrs = set()
        #vertices removed from non_nbrs after adding the
        #last choice to the partial solution (helps speed up backtracking)
        self.removed = []


def get_instance(n, p=0.3):
    """
    gets an instance of the independent set problem.
    """
    return networkx.fast_gnp_random_graph(n, p)


class MaxIndependentSetBB:
    """
    Branch and bound implementation for the max independent set problem
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
        the current independent set can not be enlarged.
        """
        # TODO
        pass

    def bound(self, subproblem) -> float:
        """
        Bound the potential solution quality of the (implicit) subtree rooted
        at the current subproblem.

        Recall that the subproblem represents a node in an implicit
        search tree. In the case of Independent set, this function
        should return an upper bound on the maximum size of any (valid)
        independent set subproblem in the subtree rooted at this node

        suggestion: consider the subgraph induced by the vertices in the
        subproblem's non_nbr's set. The number of edges in this subgraph
        can be used to upper bound the number of vertices that can be added
        to the partial solution.

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
        Proposes a next choice (vertex) to include in the subproblem's partial
        solution.
        The choice of next item can be arbitrary, or it can depend in some way
        on the current subproblem.
        For example, when choosing the next item to consider, you could choose
        (1) a vertex not in the partial solution with minumum degree in G[non_nbrs]
        """
        # TODO
        pass

    def solve(self, G):
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

        # get the next choice (vertex) that should be added
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


class MaxIndependentSet:
    """
    Brute force implementation of max independent set problem.

    Feel free to use subroutines from assignment1 here
    """

    def solve(self, G):
        # TODO
        pass
