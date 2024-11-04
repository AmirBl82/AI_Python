import networkx as nx
from queue import LifoQueue

stack = LifoQueue()

def dfs_target(graph, start_node, target):
    frontier = stack
    frontier.put((start_node, [start_node]))
    explored = set()

    while not frontier.empty():
        current_node, path = frontier.get()

        if current_node == target:
            return f"Target {target} found, path: {'->'.join(path)}"
        
        if current_node not in explored:
            explored.add(current_node)

            for neighbor in graph.neighbors(current_node):
                if neighbor not in explored:
                    new_path = path + [neighbor]
                    frontier.put((neighbor, new_path))
    
    return f"Target {target} not found"

Graph = nx.Graph()
edges = [('A', 'B'), ('A', 'C'),
         ('B', 'D'), ('B', 'C'), ('B', 'E'),
         ('C', 'D'), ('C', 'E'), ('D', 'E')]
Graph.add_edges_from(edges)

print(dfs_target(Graph, 'A', 'D'))