# --- Day 13: Transparent Origami ---
#
# https://adventofcode.com/2021/day/13

import requests


def origami_v1(origami_raw):
    dots, instructions = __extract_data(origami_raw)
    dots = __fold(dots, instructions, False)
    return len(dots)


def origami_v2(origami_raw):
    dots, instructions = __extract_data(origami_raw)
    dots = __fold(dots, instructions, True)
    __print_dots(dots)
    return None


def __print_dots(dots):
    dots_map = __construct_dot_map(dots)
    row_index = 0
    while row_index < len(dots_map.keys()):
        columns = dots_map.get(row_index)
        max_x = __find_max_x(columns)
        col_index = 0
        line = ""
        while col_index <= max_x:
            if col_index in columns:
                line = line + "#"
            else:
                line = line + "."
            col_index += 1
        print(line)
        row_index += 1
    return None


def __construct_dot_map(dots):
    dots_map = dict()
    for dot in dots:
        x = int(dot.split(',')[0])
        y = int(dot.split(',')[1])
        c_l = dots_map.get(y, set())
        c_l.add(x)
        dots_map[y] = c_l
    return dots_map


def __find_max_x(columns):
    max_x = 0
    for col in columns:
        if int(col) > max_x:
            max_x = int(col)
    return max_x


def __fold(dots, instructions, fold_all):
    for instruction in instructions:
        if 'y=' in instruction:
            dots = __fold_up(dots, int(instruction.split('=')[1]))
        else:
            dots = __fold_left(dots, int(instruction.split('=')[1]))
        if not fold_all:
            break
    return dots


def __fold_left(dots, fold_line):
    new_dots = set()
    for dot in dots:
        x = int(dot.split(',')[0])
        if x < fold_line:
            new_dots.add(dot)
        else:
            delta = x - fold_line
            new_dots.add(str(fold_line - delta) + ',' + dot.split(',')[1])
    return new_dots


def __fold_up(dots, fold_line):
    new_dots = set()
    for dot in dots:
        y = int(dot.split(',')[1])
        if y < fold_line:
            new_dots.add(dot)
        else:
            delta = y - fold_line
            new_dots.add(dot.split(',')[0] + ',' + str(fold_line - delta))
    return new_dots


def __extract_data(raw):
    dots = set()
    instructions = list()
    is_dot = True
    for row in raw:
        if row == '':
            is_dot = False
            continue
        if is_dot:
            dots.add(row)
        else:
            instructions.append(row)
    return dots, instructions


if __name__ == '__main__':
    m_headers = {
        'cookie': '<COOKIE HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/13/input", headers=m_headers).text.splitlines()
    file_input = open('origami_folding_instructions.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(origami_v1(file_input)))
    print("Part: 2 = " + str(origami_v2(url_input)))
