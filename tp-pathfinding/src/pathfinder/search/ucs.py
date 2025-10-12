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

            node = frontier.pop()
            print(node.state)

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                state = grid.result(node.state, action)
                cos = node.cost + grid.individual_cost(node.state, action)

                if state not in reached or cos < reached[state]:
                    new_node = Node("", state, cos, node, action)
                    print(new_node.state)
                    reached[state] = cos
                    frontier.add(new_node, cos)

        return NoSolution(reached)
