# Day 16: Chiton  - Problem 1
import numpy as np
from collections import Counter
import networkx as nx

"""
Hex codes - for part 1, if we can find all the packets and keep track of their version numbers,
we are done. Don't need to parse the literal values. Just find the packets.
"""

test = False
mini = False

if test:
    if not mini:
        data_file = f'data/example.txt'
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

def len_of_n_subpackets(packets, n):
    pos = 0
    num_packets = 0
    while num_packets < n:
        version_num, type_num = get_version_type(packets, pos)
        pos += 6


def process_packet_tree(G, packet, pos, type1hunting=0):
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
    while packet_length > pos or (type1hunting > 0 and num_packets_found < type1hunting):
        # Check if nothing left but trailing zeroes
        if all(bit == '0' for bit in packet[pos:]):
            pos = packet_length + 1
            break

        version_num, type_num = get_version_type(packet, pos)
        print(f'version_num {version_num}, type_num {type_num}')
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

            print(f'literal_bin {literal_bin} --> {int(literal_bin, 2)}')
            packet_num = G.number_of_nodes() + 1
            G.add_node(packet_num, type_num=type_num, version_num=version_num, pos=pos)
            G.add_edge(packet_num - 1, packet_num)
            num_packets_found += 1
            # Check if this literal has trailing zeroes
            print(pos)
            print(packet[pos:])
            if all(bit == '0' for bit in packet[pos:]):
                pos = packet_length + 1
        else:
            # Operator packet

            # Length type ID is bit immediately after packet header
            len_type_id = packet[pos]
            pos += 1
            if len_type_id == '0':
                # Get next 15 bits
                len_subpackets = int(packet[pos:pos+15], 2)
                pos += 15
                packet_start = pos
                packet_end = packet_start + len_subpackets
                new_packets = packet[packet_start:packet_end]
                print(new_packets)
                packet_num = G.number_of_nodes() + 1
                G.add_node(packet_num, type_num=type_num, version_num=version_num, pos=pos)
                G.add_edge(packet_num - 1 , packet_num)
                num_packets_found += 1

                G = process_packet_tree(G, new_packets, 0)
                pos += len_subpackets
                print(packet[pos:])

            else:
                # Get next 11 bits
                num_subpackets = int(packet[pos:pos+11], 2)
                pos += 11
                print(packet[pos:])
                packet_num = G.number_of_nodes() + 1
                G.add_node(packet_num, type_num=type_num, version_num=version_num, pos=pos)
                #G.add_edge(packet_num, packet_num + 1)
                num_packets_found += 1

                # For part 1, let's just ignore this type and plunge forward
                # Don't actually need to deal with it since we just need to find
                # all packets eventually
                #pos = process_packet_tree(G, packet, packet_num, pos)

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
        G.add_node(packet_num, type_num=0, version_num=0, pos=0)
        G = process_packet_tree(G, bin_packet, pos)


        version = nx.get_node_attributes(G, 'version_num')
        tot_version = sum([v for k, v in version.items()])
        print(tot_version)
        for k, v in version.items():
            print(f'node {k}, version_num {v}')



        # tot_version_num = 0
        # version_num, type_num = get_version_type(bin_packet, pos)
        # tot_version_num += version_num
        # pos += 6
        # # print(f'packet version: {version_code} --> {version_num}')
        # # print(f'packet type: {type_code} --> {type_num}')
        #
        # # Process this packet
        # total_version_num = process_packet(bin_packet, tot_version_num)










