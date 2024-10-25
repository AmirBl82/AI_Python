from collections import deque
import networkx as nx

def bfs_target(graph, start_node, target):
    frontier = deque([(start_node, [start_node])])
    explored = set()
    
    while frontier:
        current_node, path = frontier.popleft()

        if current_node == target:
            return f"Target '{target}' found, path: {'->'.join(path)}"
        else:
            for neighbor in graph.neighbors(current_node):
                if neighbor not in explored:
                    explored.add(neighbor)
                    new_path = path + [neighbor]
                    frontier.append((neighbor, new_path))
                
    return f"Target '{target}' not found"

Graph = nx.Graph()
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'A'), ('B', 'D'),
    ('C', 'B'), ('C', 'F'),
]
Graph.add_edges_from(edges)

print(bfs_target(Graph, 'A', 'F'))
print(bfs_target(Graph, 'A', 'G'))
