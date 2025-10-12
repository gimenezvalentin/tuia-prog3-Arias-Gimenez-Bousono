from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        frontier.add(root, root.cost + grid.hmanhattan(root))
        
        while not frontier.is_empty():
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):

                state = grid.result(node.state, action)
                cos = node.cost + grid.individual_cost(node.state, action)

                print(state, cos)

                if state not in reached or cos < reached[state]:
                    new_node = Node("", state, cos, node, action)
                    reached[state] = cos
                    frontier.add(new_node, new_node.cost + grid.hmanhattan(new_node))

                    print(new_node)


                    
        return NoSolution(reached)
