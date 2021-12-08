# Day 8 - Problem 2
import numpy as np
import itertools

def run():
    test = False

    if test:
        data_file = 'data/example.txt'
    else:
        data_file = 'data/input.txt'

    wires = {'a': '',
             'b': '',
             'c': '',
             'd': '',
             'e': '',
             'f': '',
             'g': ''}

    valid_numbers = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

    final_value = 0
    with open(data_file, 'r') as file_input:
        for line in file_input:
            sig_out = line.split('|')
            signals = sig_out[0].strip().split(' ')
            outputs = sig_out[1].strip().split(' ')
            sig_lens = [len(s) for s in signals]
            sig_nums = [-1 for s in signals]

            valid_decoder = brute_force_find_valid_decoder(signals, outputs)
            # Use decoder to get correctly wired readout
            decoded_readouts = [decode_signal(out, valid_decoder) for out in outputs]
            # Convert decoded readouts to list of digit strings
            values = [str(translate_readout(cv)) for cv in decoded_readouts]
            # Convert digit string list into integer
            value = int(''.join(values))
            # Increment running total of values
            final_value += value

            # # Find the 1's (len2)
            # len2_idx = sig_lens.index(2)
            # if len2_idx > -1:
            #     set1 = set([s for s in signals[len2_idx]])
            #     wires['c'] = set1
            #     wires['f'] = set1
            #     print(wires)
            #
            # # Find the 7's (len3)
            # len3_idx = sig_lens.index(3)
            # if len3_idx > -1:
            #     set7 = set(signals[len3_idx])
            #     wires['a'] = set7 - set1
            #
            #     print(wires)
            #
            #     # Find the 4's (len4)
            #     len4_idx = sig_lens.index(4)
            #     if len4_idx > -1:
            #         set4 = set(signals[len4_idx])
            #         wires['b'] = set4 - set1
            #         wires['d'] = set4 - set1
            #
            #         print(wires)
            #
            # break

    print(final_value)


def brute_force_find_valid_decoder(signals, outputs):
    """
    Create all possible mappings and look for a valid set of numeric output
    :return:
    """

    letters = 'abcdefg'
    mappings = itertools.permutations(letters)

    valid_mappings = set()
    for m in mappings:
        decoder = {m[i]: letters[i] for i in range(7)}
        valid = True
        for s in signals:
            # Check if this signal converts to a valid readout for this decoder
            if decode_signal(s, decoder) is None:
                valid = False
                break
        if valid:
            valid_mappings.add(m)

    vm = valid_mappings.pop()
    decoder = {vm[i]: letters[i] for i in range(7)}
    print(decoder)
    return decoder


def decode_signal(signal, decoder):
    """
    Use decoder to convert signal to valid number readout. Return None if impossible.
    :param signal:
    :param decoder:
    :return:
    """
    valid_numbers = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    #print(signal)
    readout = ''.join(sorted([decoder[s] for s in signal]))
    if readout in valid_numbers:
        return readout
    else:
        return None


def translate_readout(readout):

    valid_numbers = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    value = valid_numbers.index(readout)
    return value


if __name__ == '__main__':
    run()
    output = decode_signal('ab', {'d': 'a', 'e': 'b',
                                  'a': 'c',
                                  'f': 'd',
                                  'g': 'e',
                                  'b': 'f',
                                  'c': 'g'})
    #print(output)









