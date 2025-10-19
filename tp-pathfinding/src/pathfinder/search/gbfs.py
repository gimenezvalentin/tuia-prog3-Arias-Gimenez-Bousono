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
        #la prioridad del nodo en la frontera es SOLO
        # la función heurística (h(n)), ignorando el costo real acumulado (g(n))!!!
        frontier.add(root, grid.hmanhattan(root))
        

        while not frontier.is_empty():
            #El nodo extraido es el que parece estar mas cerca del objetivo,
            #segun la estimación heurística 
            node = frontier.pop()
            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                state = grid.result(node.state, action)
                #'cos' (costo acumulado) se calcula pero SOLO se usa para actualizar 'reached'!
                #NO! se usa para ordenar la frontera
                cos = node.cost + grid.individual_cost(node.state, action)
                #A diferencia de A*, la condición de reemplazo
                #aca es solo para evitar ciclos infinitos, no para garantizar el menor costo
                if state not in reached or cos < reached[state]:
                    new_node = Node("", state, cos, node, action)
                    reached[state] = cos
                    #Añadimos el nuevo nodo a la frontera
                    #Su prioridad es grid.h(new_node), que es la función heurística (h(n))
                    frontier.add(new_node, grid.hmanhattan(new_node))
                    
        return NoSolution(reached)
