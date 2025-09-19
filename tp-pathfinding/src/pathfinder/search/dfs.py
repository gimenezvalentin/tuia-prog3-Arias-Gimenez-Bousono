from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        if grid.objective_test(root.state):
            return Solution(root)
        
        # Initialize explored with the initial state
        explored = {}
        explored[root.state] = True

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)
        
        while not frontier.is_empty():
            n = frontier.remove()
            # if n.state in explored:
            #     continue
            explored[n.state] = True
            for a in grid.actions(n.state):
                s = grid.result(n.state,a)
                if s not in explored:
                    m = Node("", s, n.cost + grid.individual_cost(n.state, a), n, a)
                    if grid.objective_test(s):
                        return Solution(m, explored)
                    frontier.add(m)

        return NoSolution(explored)
