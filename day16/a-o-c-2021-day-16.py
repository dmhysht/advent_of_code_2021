# --- Day 16: Packet Decoder ---
#
# https://adventofcode.com/2021/day/16

import numpy
import requests

BITS = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
        '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def decode_v1(encoded):
    decoded = __decode(encoded)
    ret = __do_decode(0, len(decoded), -1, decoded)
    print("Iter: " + str(ret[0]) + "; Version Sum: " + str(ret[1]) \
        + "; Literals: " + str(ret[2]))
    return str(ret[1])


def decode_v2(encoded):
    decoded = __decode(encoded[0])
    ret = __do_decode(0, len(decoded), -1, decoded)
    print("Iter: " + str(ret[0]) + "; Version Sum: " + str(ret[1]) \
        + "; Literals: " + str(ret[2]))
    return str(ret[2][0])


def __do_decode(i, end, end_counter, decoded):
    v_sum = 0
    literals = list()
    while end != -1 and i < end or end_counter != -1 and len(literals) < end_counter:
        i, v, t = __get_v_and_t(i, decoded)
        v_sum += v
        if t == 4:
            i, literal = __handle_literal(i, decoded)
            literals.append(literal)
        elif t != -1:
            i, v, literals_ret = __do_handle_operator(i, decoded)
            if t == 0:
                res = sum(literals_ret)
            elif t == 1:
                res = numpy.prod(literals_ret)
            elif t == 2:
                res = min(literals_ret)
            elif t == 3:
                res = max(literals_ret)
            elif t == 5:
                res = 1 if literals_ret[0] > literals_ret[1] else 0
            elif t == 6:
                res = 1 if literals_ret[0] < literals_ret[1] else 0
            else:
                res = 1 if literals_ret[0] == literals_ret[1] else 0
            literals.append(res)
            v_sum += v
    return i, v_sum, literals


def __get_v_and_t(i, decoded):
    if len(decoded) - i <= 6:
        return len(decoded), 0, -1
    b_ver = decoded[i: i + 3]
    b_type = decoded[i + 3: i + 6]
    return i + 6, int(b_ver, 2), int(b_type, 2)


def __handle_literal(i, decoded):
    if i >= len(decoded):
        return i, 0
    done = False
    last_group = False
    counting = False
    collecting_counter = 0
    b_collector = ""
    while not done:
        if not counting:
            if decoded[i] == '0':
                last_group = True
            counting = True
        else:
            if collecting_counter == 4:
                if last_group:
                    done = True
                    continue
                collecting_counter = 0
                counting = False
                continue
            else:
                b_collector += decoded[i]
                collecting_counter += 1
        i += 1

    return i, int(b_collector, 2)


def __do_handle_operator(i, decoded):
    if i + 1 >= len(decoded):
        return i + 1, 0, []
    zero_type = decoded[i] == '0'
    if zero_type:
        bits = 15
    else:
        bits = 11
    i += 1
    size_iter = min(i + bits, len(decoded))
    b_length_collector = ""
    while i < size_iter:
        b_length_collector += decoded[i]
        i += 1
    length = int(b_length_collector, 2)
    if zero_type:
        end = i + length
        return __do_decode(i, end, -1, decoded)
    else:
        return __do_decode(i, -1, length, decoded)


def __decode(encoded):
    decoded = ""
    for line in encoded:
        for hexa in line:
            decoded += BITS.get(hexa)
    return decoded


if __name__ == '__main__':
    m_headers = {
        'cookie': '<COOKIE HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/16/input", headers=m_headers).text.splitlines()
    file_input = open('encoded_msg.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(decode_v1(file_input)))
    print("Part: 2 = " + str(decode_v2(file_input)))
