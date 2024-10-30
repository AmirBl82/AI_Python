from queue import Queue
import networkx as nx
def bfs_target(graph,start_node,target):
    frontier = Queue([start_node])

    while frontier:
        current_node = frontier.get()

        if current_node == target:
            return f"Target '{target} found"
        else:
            for neighbor in graph.neighbors(current_node):
                frontier.put(neighbor)
                
    
    return f"Target '{target}' not found"
    

Graph = nx.Graph()
edges = [
    ('A','B'), ('A','C'),
    ('B','A'), ('B', 'D'),
    ('C','B'), ('C','F'),
]
Graph.add_edges_from(edges)

print(bfs_target(Graph,'A','F'))
print(bfs_target(Graph,'A','G'))