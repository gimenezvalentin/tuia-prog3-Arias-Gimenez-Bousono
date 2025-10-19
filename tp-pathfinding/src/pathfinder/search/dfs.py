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
        #'Explored' (Explorado) se usa para evitar ciclos
        # y re-visitar estados, garantizando que el algoritmo termine!!
        explored = {}

        # Initialize frontier with the root node
        #implementada como una Pila, que garantiza un comportamiento LIFO
        frontier = StackFrontier()
        frontier.add(root)
        
        while not frontier.is_empty():
            #Al usar 'remove()' en una pila, se extrae el nodo añadido más recientemente
            #Esto fuerza la exploración de la rama más profunda primero!!!
            node = frontier.remove()

            if node.state in explored: #Condicion para saltar (continuar) si el estado ya fue explorado
                continue
            
            #Marcamos el estado del nodo actual como explorado
            explored[node.state] = True
            
            for action in grid.actions(node.state):
                state = grid.result(node.state, action)

                if state not in explored: #Solo consideramos estados que no hayan sido explorados
                    #El costo (node.cost...) se calcula, pero DFS NO lo utiliza para la ordenación
                    new_node = Node("", state, node.cost + grid.individual_cost(node.state, action), node, action)
                    
                    #La prueba de objetivo se realiza al generar el sucesor (mientras se expande)
                    if grid.objective_test(state):
                        return Solution(new_node, explored)
                    
                    frontier.add(new_node) #sera el proximo en ser expandido

        return NoSolution(explored)
