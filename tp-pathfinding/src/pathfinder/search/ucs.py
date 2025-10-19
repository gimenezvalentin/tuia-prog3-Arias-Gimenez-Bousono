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
        frontier.add(root, root.cost)  #El costo real es la prioridad
        
        while not frontier.is_empty():

            node = frontier.pop()
           #El test objetivo se realiza al extraer el nodo, no al insertarlo (a diferencia de BFS),
            # para asegurar que hemos encontrado el camino de menor costo!!

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                state = grid.result(node.state, action)
                #Calculo del costo real, costo del nodo padre + costo individual de la accion
                cos = node.cost + grid.individual_cost(node.state, action) 
                
                #Revisitamos un estado si encontramos un camino más barato, clave para la optimalidad!!
                if state not in reached or cos < reached[state]:
                    new_node = Node("", state, cos, node, action)
                    reached[state] = cos #Actualizamos el registro de costo más bajo
                    frontier.add(new_node, cos) #Añadimos el nuevo nodo a la Frontier con el costo acumulado como su prioridad

        return NoSolution(reached)
