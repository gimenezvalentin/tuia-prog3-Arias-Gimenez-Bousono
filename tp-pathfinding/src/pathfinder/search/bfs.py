from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        if grid.objective_test(root.state):
            return Solution(root, reached)
        
        # Initialize frontier with root
        frontier = QueueFrontier()
        frontier.add(root)
        # Initialize reached with the initial state
        #'Reached' (Alcanzado) se usa para marcar estados visitados
        #y evitar ciclos, asegurando que cada estado se explore solo una vez
        reached = {}
        reached[root.state] = True  #Solo almacenamos si se visito (True), no el costo

        while not frontier.is_empty():
            #Al usar 'remove()' en una cola, se extrae el nodo añadido primero
            #Esto garantiza la exploración nivel por nivel!!!!
            node = frontier.remove()
            
            #expandimos
            for action in grid.actions(node.state):
                state = grid.result(node.state, action)
                
                #Solo procesamos el estado si no ha sido visitado
                if state not in reached:
                    # El costo se calcula, pero NO se usa para ordenar la busqueda
                    new_node = Node("", state, node.cost + grid.individual_cost(node.state, action), node, action) 
                    
                    #La prueba de objetivo se realiza al generar
                    #el sucesor (mientras se expande), lo que acelera la deteccion
                    if grid.objective_test(state):
                        return Solution(new_node, reached)
                    reached[new_node.state] = True
                    frontier.add(new_node)
                    
        return NoSolution(reached)
