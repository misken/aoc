import re
import networkx as nx


small = True

if small:
    data_file = 'day7/input_small'
else:
    data_file = 'day7/input'

rgx_str = r'^(\w+\s\w+)\sbags*\scontain'
rgx = re.compile(rgx_str)

rgx_contains_str = r'\d+\s\w+\s\w+\sbags*[,\s\.]'
rgx_contains = re.compile(rgx_contains_str)

rgx_inside_str = r'(\d+)\s(\w+\s\w+)'
rgx_inside = re.compile(rgx_inside_str)

G = nx.DiGraph()
bags = set()
with open(data_file, 'r') as input:
    lines = input.read().splitlines()

for line in lines:

    # Create set of all colors by reading first two words of line
    rgx_match = re.match(rgx_str, line)

    outer_bag = rgx_match.group(1)
    if outer_bag not in G.nodes():
        G.add_node(outer_bag)
        bags.add(outer_bag)

    contains_list = rgx_contains.findall(line)

    for bag in contains_list:
        bag_match = rgx_inside.match(bag)
        num_bags = bag_match.group(1)
        bag_color = bag_match.group(2)

        if bag_color not in G.nodes():
            G.add_node(bag_color)
            bags.add(bag_color)

        G.add_edge(outer_bag, bag_color, num_bags=num_bags)


all_bags = [G.nodes['shiny gold']]
num_bags = 1

new_bags = [n for n in G['shiny gold']]
print(new_bags)



