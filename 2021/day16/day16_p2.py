# Day 16: Chiton  - Problem 2
import numpy as np
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

"""
Hex codes - for part 1, if we can find all the packets and keep track of their version numbers,
we are done. Don't need to parse the literal values. Just find the packets.

Now for part 2, we need to deal with the type 1 operators and build the tree to be able to
traverse it and do the math
"""

test = False
mini = False

if test:
    if not mini:
        data_file = f'data/example2.txt'
    else:
        data_file = f'data/mini_example.txt'

else:
    data_file = 'data/input.txt'

def get_version_type(packets, pos):
    version_code = packets[pos:pos + 3]
    version_num = int(version_code, 2)

    pos += 3
    type_code = packets[pos:pos + 3]
    type_num = int(type_code, 2)

    return version_num, type_num

def find_unfulfilled_operator(G, n):
    unfulfilled_operator = None
    node = n - 1
    while node >= 2:
        #print(f'node {node} {G.nodes[node]}')
        if G.nodes[node]['len_type_id'] == 1:
            num_subpackets_found = len([s for s in G.successors(node)])
            if num_subpackets_found < G.nodes[node]['num_subpackets']:
                # Haven't found all the subpackets, add edge to predecessor
                unfulfilled_operator = node
                return unfulfilled_operator
        elif G.nodes[node]['len_type_id'] == 0:
            if G.nodes[n]['pos'] < G.nodes[node]['packet_end'] + 2:
                unfulfilled_operator = node
                return unfulfilled_operator


        node -= 1

    return unfulfilled_operator



def value_of_node(G, n):
    type_num = G.nodes[n]['type_num']

    if type_num == 0:
        value = np.sum([value_of_node(G, s) for s in G.successors(n)])
    elif type_num == 1:
        # Product node
        value = np.prod([value_of_node(G, s) for s in G.successors(n)])
    elif type_num == 2:
        # Min node
        value = np.min([value_of_node(G, s) for s in G.successors(n)])
    elif type_num == 3:
        # Max node
        value = np.max([value_of_node(G, s) for s in G.successors(n)])
    elif type_num == 4:
        # Literal value
        value = G.nodes[n]['value']
    elif type_num == 5:
        # > node
        sub_nodes = [s for s in G.successors(n)]
        if G.nodes[sub_nodes[0]]['pos'] < G.nodes[sub_nodes[1]]['pos']:
            n1, n2 = sub_nodes[0], sub_nodes[1]
        else:
            n2, n1 = sub_nodes[0], sub_nodes[1]

        if value_of_node(G, n1) > value_of_node(G, n2):
            value = 1
        else:
            value = 0

    elif type_num == 6:
        # < node
        sub_nodes = [s for s in G.successors(n)]
        if G.nodes[sub_nodes[0]]['pos'] < G.nodes[sub_nodes[1]]['pos']:
            n1, n2 = sub_nodes[0], sub_nodes[1]
        else:
            n2, n1 = sub_nodes[0], sub_nodes[1]

        if value_of_node(G, n1) < value_of_node(G, n2):
            value = 1
        else:
            value = 0
    elif type_num == 7:
        # == node
        sub_nodes = [s for s in G.successors(n)]
        if G.nodes[sub_nodes[0]]['pos'] < G.nodes[sub_nodes[1]]['pos']:
            n1, n2 = sub_nodes[0], sub_nodes[1]
        else:
            n2, n1 = sub_nodes[0], sub_nodes[1]

        if value_of_node(G, n1) == value_of_node(G, n2):
            value = 1
        else:
            value = 0
    else:
        print(f'Unknown node type {type_num}')
        exit(1)

    return value


def process_packet_tree(G, packet, pos, predecessor=None):
    """
    Not sure if this will be called once or used somewhat recursively

    :param packet:
    :param packet_num:
    :param pos:
    :return:
    """

    #unresolved_nodes = []  # List of operator nodes that haven't been explored (can this even happen?)


    #unresolved_nodes.append(G.nodes[packet_num])
    packet_length = len(packet)
    num_packets_found = 0
    while packet_length > pos:
        # Check if nothing left but trailing zeroes
        if all(bit == '0' for bit in packet[pos:]):
            pos = packet_length + 1
            G.nodes[1]['pos'] = pos
            break

        version_num, type_num = get_version_type(packet, pos)
        pos += 6

        if type_num == 4:
            # Process literal value
            leading_0 = False
            literal_bin = ''
            while not leading_0:
                chunk = packet[pos: pos + 5]
                literal_bin += chunk[1:]
                if chunk[0] == '0':
                    leading_0 = True
                pos += 5
            node_value = int(literal_bin, 2)
            #print(f'literal_bin {literal_bin} --> {node_value}')
            packet_num = G.number_of_nodes() + 1
            G.add_node(packet_num, type_num=type_num, version_num=version_num, len_type_id=-1,
                       pos=pos, predecessor=predecessor, node_color='red', value=node_value)
            G.nodes[1]['pos'] = pos
            #print(f'node {packet_num}, version {version_num}, type {type_num}')
            pred_node = find_unfulfilled_operator(G, packet_num)
            if pred_node is not None:
                G.add_edge(pred_node, packet_num)


            # Check if this literal has trailing zeroes
            # print(pos)
            # print(packet[pos:])
            # if all(bit == '0' for bit in packet[pos:]):
            #     pos = packet_length + 1
            #     G.nodes[1]['pos'] = pos
        else:
            # Operator packet

            # Length type ID is bit immediately after packet header
            len_type_id = int(packet[pos])
            pos += 1
            G.nodes[1]['pos'] = pos
            if len_type_id == 0:
                # Get next 15 bits
                len_subpackets = int(packet[pos:pos+15], 2)
                pos += 15
                G.nodes[1]['pos'] = pos
                packet_start = pos
                packet_end = packet_start + len_subpackets
                new_packets = packet[packet_start:packet_end]
                # print(new_packets)
                packet_num = G.number_of_nodes() + 1
                G.add_node(packet_num, type_num=type_num, version_num=version_num, pos=pos,
                           len_type_id=len_type_id, predecessor=predecessor, packet_end=packet_end,
                           node_color='blue', value=0)
                #print(f'node {packet_num}, version {version_num}, type {type_num}')
                pred_node = find_unfulfilled_operator(G, packet_num)
                if pred_node is not None:
                    G.add_edge(pred_node, packet_num)

                #G = process_packet_tree(G, new_packets, 0, predecessor=packet_num)
                G = process_packet_tree(G, packet, pos, predecessor=packet_num)
                #pos += len_subpackets
                pos = G.nodes[1]['pos']
                #print(packet[pos:])

            else:
                # Get next 11 bits
                num_subpackets = int(packet[pos:pos+11], 2)
                pos += 11
                G.nodes[1]['pos'] = pos
                #print(packet[pos:])
                packet_num = G.number_of_nodes() + 1
                G.add_node(packet_num, type_num=type_num, version_num=version_num, pos=pos,
                           predecessor=predecessor,
                           len_type_id=len_type_id, num_subpackets=num_subpackets,
                           node_color='green', value=0)
                #print(f'node {packet_num} {G.nodes[packet_num]}')
                pred_node = find_unfulfilled_operator(G, packet_num)
                if pred_node is not None:
                    G.add_edge(pred_node, packet_num)

                G = process_packet_tree(G, packet, pos, predecessor=packet_num)
                pos = G.nodes[1]['pos']
                #print(packet[pos:])

    return G

with open(data_file, 'r') as file_input:

    hex_packets = [hp.rstrip() for hp in file_input.readlines()]
    print(f'{len(hex_packets)} packets')
    for hp in hex_packets:
        bin_packet = ''.join([format(int(s, 16), '04b') for s in hp])
        print(hp)
        print(bin_packet)
        pos = 0
        packet_num = 0

        G = nx.DiGraph()
        # Add root node
        packet_num = G.number_of_nodes() + 1
        G.add_node(packet_num, type_num=0, version_num=0, pos=0, predecessor=None, len_type_id=None, value=0)
        G = process_packet_tree(G, bin_packet, pos, predecessor=1)


        version = nx.get_node_attributes(G, 'version_num')
        tot_version = sum([v for k, v in version.items()])
        print(tot_version)
        # for k, v in version.items():
        #     print(f'node {k}, version_num {v}')

        #nx.draw(G, with_labels=True, node_size=25)
        #print([e for e in G.edges])
        print(G)
        print([n for n in G.nodes])
        print([e for e in G.edges])
        final_value = value_of_node(G, 2)
        print(f'final value = {final_value}')
        #nx.draw_networkx(G, with_labels=True)
        #plt.show()



        # tot_version_num = 0
        # version_num, type_num = get_version_type(bin_packet, pos)
        # tot_version_num += version_num
        # pos += 6
        # # print(f'packet version: {version_code} --> {version_num}')
        # # print(f'packet type: {type_code} --> {type_num}')
        #
        # # Process this packet
        # total_version_num = process_packet(bin_packet, tot_version_num)










