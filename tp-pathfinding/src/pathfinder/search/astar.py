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
        #'Reached' almacena el menor costo real (g(n)) conocido para llegar a cada estado
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        #f(n) = g(n) + h(n) 
        #g(n) es root.cost y h(n) es grid.hmanhattan(root).
        frontier.add(root, root.cost + grid.hmanhattan(root))
        
        while not frontier.is_empty():
            #El nodo extraido es siempre el que tiene el menor costo TOTAL ESTIMADO (f(n))
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):

                state = grid.result(node.state, action)
                #g(n): Costo real acumulado para llegar al sucesor
                cos = node.cost + grid.individual_cost(node.state, action)

                #Solo procesamos si encontramos el estado por primera vez O si el nuevo
                #camino tiene un costo REAL (g(n)) menor que el previamente registrado
                if state not in reached or cos < reached[state]:
                    new_node = Node("", state, cos, node, action)
                    #Actualizamos el menor costo real conocido (g(n))
                    reached[state] = cos
                    #Añadimos el nodo a la frontera usando la 
                    # función f(n) como su prioridad
                    frontier.add(new_node, new_node.cost + grid.hmanhattan(new_node))


                    
        return NoSolution(reached)
