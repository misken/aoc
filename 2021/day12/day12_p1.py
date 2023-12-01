# Day 12: Passage pathing  - Problem 1
import numpy as np
from collections import Counter
import networkx as nx

"""
Do a depth first search and don't allow multiple visits to small caves (keep track with Counter).
"""
test = True
test_size = 'mini'
test_size = 'middle'
test_size = 'larger'

if test:
    data_file = f'data/{test_size}_example.txt'
else:
    data_file = 'data/input.txt'

with open(data_file, 'r') as file_input:
    lines = file_input.readlines()
    edges = [line.strip().split('-') for line in lines]
    print(edges)


G = nx.Graph()
for edge in edges:
    node1, node2 = edge[0], edge[1]
    G.add_edge(node1, node2)
print(G)

# Try to find paths
# Initialize partial paths to explore
paths = []
to_explore = []
for node in G.adj['start']:
    to_explore.append(['start', node])

while len(to_explore) > 0:
    current_path = to_explore.pop()
    terminal_node = current_path[-1]
    new_neighbors = G.adj[terminal_node]
    for n in new_neighbors:
        if n == 'end':
            complete_path = current_path.copy()
            complete_path.append('end')
            paths.append(complete_path)
            print(complete_path)
        else:
            if n.isupper() or Counter(current_path)[n] == 0:
                new_partial_path = current_path.copy()
                new_partial_path.append(n)
                to_explore.append(new_partial_path)

print(paths)
print(len(paths))




