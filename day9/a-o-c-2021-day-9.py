# --- Day 9: Smoke Basin ---
#
# https://adventofcode.com/2021/day/9

import requests


def risk_eval_v1(heightmap):
    lowest_points_coords = __get_lowest_points_coord(heightmap)
    total_risk = 0
    for lowest_point_coord in lowest_points_coords:
        total_risk = total_risk + (1 + int(heightmap[lowest_point_coord[0]][lowest_point_coord[1]]))
    return total_risk


def risk_eval_v2(heightmap):
    lowest_points_coords = __get_lowest_points_coord(heightmap)
    basins = list()
    for lowest_points_coord in lowest_points_coords:
        basins.append(__find_basin_len(lowest_points_coord, heightmap))
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


def __find_basin_len(seed_coordinate, heightmap):
    basin_coords = set()
    __recursive(seed_coordinate, basin_coords, heightmap)
    return len(basin_coords)


def __recursive(coord, basin_coords, heightmap):
    basin_coords.add(str(coord[0]) + str(coord[1]))
    adj_h = __retrieve_adjacent_heights(coord[0], coord[1], heightmap)
    for val in adj_h:
        if val[0] < 9:
            coord = str(val[1][0]) + str(val[1][1])
            if coord not in basin_coords:
                __recursive(val[1], basin_coords, heightmap)


def __get_lowest_points_coord(heightmap):
    lowest_points_coords = list()
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[i])):
            if __is_lowest_point(i, j, heightmap):
                lowest_points_coords.append([i, j])
    return lowest_points_coords


def __is_lowest_point(i, j, heightmap):
    curr_height = int(heightmap[i][j])
    adjacent_heights = __retrieve_adjacent_heights(i, j, heightmap)
    if __lowest_among_adj(curr_height, adjacent_heights):
        return True
    return False


def __retrieve_adjacent_heights(i, j, heightmap):
    adjacent_heights = list()
    if j > 0:
        adjacent_heights.append((int(heightmap[i][j - 1]), [i, j - 1]))
    if j < len(heightmap[i]) - 1:
        adjacent_heights.append((int(heightmap[i][j + 1]), [i, j + 1]))
    if i > 0:
        adjacent_heights.append((int(heightmap[i - 1][j]), [i - 1, j]))
    if i < len(heightmap) - 1:
        adjacent_heights.append((int(heightmap[i + 1][j]), [i + 1, j]))
    return adjacent_heights


def __lowest_among_adj(curr_height, adjacent_heights):
    for adj_height in adjacent_heights:
        if adj_height[0] <= curr_height:
            return False
    return True


if __name__ == '__main__':
    m_headers = {
        'cookie': '_ga=GA1.2.1019470197.1641915265; _gid=GA1.2.1126259102.1671810120; session=53616c7465645f5f8bd539a7424636231369f415660cfc79caa8fb56510b51c6eb798681d4bd9484de8764dde352c3256d7a85c0d67955501fecd5282c51b383'}
    url_input = requests.get("https://adventofcode.com/2021/day/9/input", headers=m_headers).text.splitlines()
    file_input = open('heightmap.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(risk_eval_v1(url_input)))
    print("Part: 2 = " + str(risk_eval_v2(url_input)))
