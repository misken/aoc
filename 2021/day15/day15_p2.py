# Day 15: Chiton  - Problem 1
import numpy as np
from collections import Counter
import networkx as nx

"""
Shortest path problem
"""

def neighbors(i, j):
    """Assumes matrix is padded with values all around; i.e. i and j are never 0"""

    neighbor_list = []

    up = i - 1, j
    down = i + 1, j
    left = i, j - 1
    right = i, j + 1

    neighbor_list.extend([up, down, left, right])

    return neighbor_list

def risk_delta(x):
    if x < 9:
        return x + 1
    else:
        return 1

def create_new_tile(m):

    new_tile = np.vectorize(risk_delta)(m)
    return new_tile

def create_full_map(one_tile, num_tiles):
    # Create each of new tiles to serve as first row
    row_of_tiles = [one_tile]

    for i in range(1, 10):
        new_tile = create_new_tile(row_of_tiles[i - 1])
        row_of_tiles.append(new_tile)

    # Create one matrix from row_of_tiles list
    new_mega_rows = []
    for i in range(num_tiles):
        new_mega_rows.append(np.concatenate(row_of_tiles[i:num_tiles + i], axis=1))

    for i in range(num_tiles):
        print(new_mega_rows[i].shape)

    new_mega_matrix = np.concatenate(new_mega_rows, axis=0)
    print(new_mega_matrix.shape)
    return new_mega_matrix


test = False

if test:
    data_file = f'data/example.txt'
else:
    data_file = 'data/input.txt'

with open(data_file, 'r') as file_input:
    # Read matrix of risk
    risk_levels_tile = np.array(np.genfromtxt(data_file, delimiter=1))
    print(risk_levels_tile.shape)

    # Read example full map for testing
    if test:
        example_fullmap = np.array(np.genfromtxt('data/example_fullmap.txt', delimiter=1))
        print(example_fullmap.shape)

    risk_levels = create_full_map(risk_levels_tile, 5)

    if test:
        map_diff = risk_levels - example_fullmap

    # Pad the array with 1000's to make edge cases easier (high cost)
    risk_levels = np.pad(risk_levels, 1, 'constant', constant_values=1000)




# Create graph
G = nx.DiGraph()

nrows = risk_levels.shape[0]
ncols = risk_levels.shape[1]

start = (1, 1)
end = (nrows - 2, ncols - 2)

for i in range(1, nrows - 1):
    for j in range(1, ncols - 1):
        my_neighbors = neighbors(i, j)

        G.add_node((i, j))
        for n in my_neighbors:
            G.add_node(n)
            G.add_edge((i, j), n, risk=risk_levels[n[0], n[1]])
            G.add_edge(n, (i, j), risk=risk_levels[i, j])

print(G)
shortest_path = nx.shortest_path(G, start, end, weight='risk')
shortest_path_risk = nx.path_weight(G, shortest_path, 'risk')
print(shortest_path)
print(shortest_path_risk)

# # Try to find paths
# # Initialize partial paths to explore
# paths = []
# to_explore = []
# for node in G.adj['start']:
#     to_explore.append(['start', node])
#
# while len(to_explore) > 0:
#     current_path = to_explore.pop()
#     terminal_node = current_path[-1]
#     new_neighbors = G.adj[terminal_node]
#     for n in new_neighbors:
#         if n == 'end':
#             complete_path = current_path.copy()
#             complete_path.append('end')
#             paths.append(complete_path)
#             print(complete_path)
#         else:
#             if n.isupper() or Counter(current_path)[n] == 0:
#                 new_partial_path = current_path.copy()
#                 new_partial_path.append(n)
#                 to_explore.append(new_partial_path)
#
# print(paths)
# print(len(paths))




