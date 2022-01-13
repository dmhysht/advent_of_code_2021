# --- Day 5: Hydrothermal Venture ---
#
# https://adventofcode.com/2021/day/5

import requests
from collections import defaultdict


def hydrothermal_venture_part_1(line_coords):
    lines = __interpret_input(line_coords)
    matrix = __generate_matrix(lines)
    for line in lines:
        __fill_if_horizontal(matrix, line)
        __fill_if_vertical(matrix, line)
    return __count_overlapping(matrix)


def __count_overlapping(matrix):
    count = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] != '.' and matrix[i][j] > 1:
                count = count + 1
    return count


def __fill_if_horizontal(matrix, line):
    # horizontal line
    if line[1] == line[3]:
        lowest_x = (line[0], line[2])[line[2] < line[0]]
        highest_x = (line[0], line[2])[line[2] > line[0]]
        for i in range(lowest_x, highest_x + 1):
            __mark_coord_in_matrix(matrix, [i, line[1]])


def __fill_if_vertical(matrix, line):
    # vertical line
    if line[0] == line[2]:
        lowest_y = (line[1], line[3])[line[3] < line[1]]
        highest_y = (line[1], line[3])[line[3] > line[1]]
        for i in range(lowest_y, highest_y + 1):
            __mark_coord_in_matrix(matrix, [line[0], i])


def __fill_if_diagonal(matrix, line):
    # if not vertical or horizontal then its diagonal
    if line[1] != line[3] and line[0] != line[2]:
        start = [line[0], line[1]]
        end = [line[2], line[3]]
        while start[0] != end[0] and start[1] != end[1]:
            __mark_coord_in_matrix(matrix, start)
            if start[0] > end[0]:
                start[0] = start[0] - 1
            else:
                start[0] = start[0] + 1
            if start[1] > end[1]:
                start[1] = start[1] - 1
            else:
                start[1] = start[1] + 1
        __mark_coord_in_matrix(matrix, end)


def __mark_coord_in_matrix(matrix, coord):
    if matrix[coord[1]][coord[0]] == '.':
        matrix[coord[1]][coord[0]] = 1
    else:
        matrix[coord[1]][coord[0]] = matrix[coord[1]][coord[0]] + 1


def __interpret_input(line_coords_input):
    coords_list = list()
    for line in line_coords_input:
        string_array = line.split(" -> ")
        point_a_string_array = string_array[0].split(",")
        point_b_string_array = string_array[1].split(",")
        line = [int(point_a_string_array[0]), int(point_a_string_array[1]),
                int(point_b_string_array[0]), int(point_b_string_array[1])]
        coords_list.append(line)
    return coords_list


def __generate_matrix(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        max_x_current = (line[0], line[2])[line[2] > line[0]]
        max_x = (max_x_current, max_x)[max_x > max_x_current]
        max_y_current = (line[3], line[1])[line[1] > line[3]]
        max_y = (max_y_current, max_y)[max_y > max_y_current]

    rows_arr = []
    for i in range(max_y + 1):
        columns_arr = []
        for j in range(max_x + 1):
            columns_arr.append('.')
        rows_arr.append(columns_arr)
    return rows_arr


def hydrothermal_venture_part_2(line_coords):
    lines = __interpret_input(line_coords)
    matrix = __generate_matrix(lines)
    for line in lines:
        __fill_if_horizontal(matrix, line)
        __fill_if_vertical(matrix, line)
        __fill_if_diagonal(matrix, line)
    return __count_overlapping(matrix)


if __name__ == '__main__':
    m_headers = {'cookie': '<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/5/input", headers=m_headers).text.splitlines()
    file_input = open('vape_line_coords.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(hydrothermal_venture_part_1(url_input)))
    print("Part: 2 = " + str(hydrothermal_venture_part_2(url_input)))


