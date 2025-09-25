from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)
        
        while not frontier.is_empty():
            n = frontier.pop()
            print(n.state)
            if grid.objective_test(n.state):
                return Solution(n, reached)
            for a in grid.actions(n.state):
                s = grid.result(n.state, a)
                cos = n.cost + grid.individual_cost(n.state, a)
                if s not in reached or cos < reached[s]:
                    m = Node("", s, cos, n, a)
                    print(m.state)
                    reached[s] = cos
                    frontier.add(m, cos)
        return NoSolution(reached)
