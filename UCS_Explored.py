from queue import PriorityQueue
import networkx as nx

def ucs_target(graph, start_node,target):
    frontier = PriorityQueue()
    frontier.put((0, start_node,[start_node]))     # (cost, node, path)
    explored = set()

    while not frontier.empty():
        cost, current_node, path = frontier.get()

        if current_node == target:
            return f"Target {target} found, path:{' -> '.join(path)}, cost:{cost}"
        
        if current_node not in explored:
            explored.add(current_node)

            for neighbor in graph.neighbors(current_node):
                if neighbor not in explored:
                    edge_weight = graph[current_node][neighbor].get('weight',1) 
                    new_cost = cost + edge_weight
                    new_path = path + [neighbor]
                    frontier.put((new_cost,neighbor,new_path))
    return f"Target {target} not found"

Graph = nx.Graph()
edges = [
    ('A', 'B', 2), ('A', 'C', 1),
    ('B', 'D', 4), ('C', 'F', 3),
    ('B', 'A', 2), ('C', 'B', 5),
]
Graph.add_weighted_edges_from(edges)

print(ucs_target(Graph, 'A', 'F'))
print(ucs_target(Graph, 'A', 'G'))