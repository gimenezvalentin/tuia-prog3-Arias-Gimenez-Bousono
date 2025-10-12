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
        
        # Initialize explored
        explored = {}

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)
        
        while not frontier.is_empty():

            node = frontier.remove()

            if node.state in explored:
                continue

            explored[node.state] = True
            
            for action in grid.actions(node.state):
                state = grid.result(node.state, action)

                if state not in explored:
                    new_node = Node("", state, node.cost + grid.individual_cost(node.state, action), node, action)

                    if grid.objective_test(state):
                        return Solution(new_node, explored)
                    
                    frontier.add(new_node)

        return NoSolution(explored)
