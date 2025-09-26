from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        frontier = PriorityQueueFrontier()
        frontier.add(root, grid.h(root))

        while not frontier.is_empty():
            n = frontier.pop()
            if grid.objective_test(n.state):
                return Solution(n, reached)
            
            for a in grid.actions(n.state):
                s = grid.result(n.state,a)
                cos = n.cost + grid.individual_cost(n.state, a)
                if s not in reached or cos < reached[s]:
                    m = Node("", s, cos, n, a)
                    reached[s] = cos
                    frontier.add_(m, grid.h(m))
                    
        return NoSolution(reached)
