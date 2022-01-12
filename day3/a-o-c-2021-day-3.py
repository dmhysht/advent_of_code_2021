# --- Day 3: Binary Diagnostic ---
#
# https://adventofcode.com/2021/day/3

import requests
from collections import defaultdict


def binary_diagnostic_part_1(binary):
    epsilon_binary = ""
    gama_rate_binary = ""
    for i in range(len(binary[0])):
        zero_count = 0
        for j in range(len(binary)):
            if binary[j][i] == '0':
                zero_count = zero_count + 1
        if zero_count > (len(binary) / 2):
            gama_rate_binary = gama_rate_binary + '0'
            epsilon_binary = epsilon_binary + '1'
        else:
            gama_rate_binary = gama_rate_binary + '1'
            epsilon_binary = epsilon_binary + '0'
    return int(gama_rate_binary, 2) * int(epsilon_binary, 2)


def binary_diagnostic_part_2(binary):
    return __get_oxygen_gen_rating(binary, 0) * __get_co2_scrubbing_rating(binary, 0)


def __get_oxygen_gen_rating(binary_list, bit_pos):
    if len(binary_list) == 1:
        return int(binary_list[0], 2)
    binary_dict = defaultdict(list)
    for binary in binary_list:
        binary_dict[binary[bit_pos]].append(binary)
    if len(binary_dict['1']) >= len(binary_dict['0']):
        return __get_oxygen_gen_rating(binary_dict['1'], bit_pos + 1)
    else:
        return __get_oxygen_gen_rating(binary_dict['0'], bit_pos + 1)


def __get_co2_scrubbing_rating(binary_list, bit_pos):
    if len(binary_list) == 1:
        return int(binary_list[0], 2)
    binary_dict = defaultdict(list)
    for binary in binary_list:
        binary_dict[binary[bit_pos]].append(binary)
    if len(binary_dict['0']) <= len(binary_dict['1']):
        return __get_co2_scrubbing_rating(binary_dict['0'], bit_pos + 1)
    else:
        return __get_co2_scrubbing_rating(binary_dict['1'], bit_pos + 1)


if __name__ == '__main__':
    m_headers = {'cookie': '<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/3/input", headers=m_headers).text.splitlines()
    file_input = open('binary.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(binary_diagnostic_part_1(url_input)))
    print("Part: 2 = " + str(binary_diagnostic_part_2(url_input)))


