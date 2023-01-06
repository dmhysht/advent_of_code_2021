# --- Day 11: Syntax Scoring ---
#
# https://adventofcode.com/2021/day/11

import requests


def flashing_octopuses_v1(energy_levels_raw):
    energy_levels = __transform_input(energy_levels_raw)
    flash = 0
    for _ in range(100):
        flashed_coords = __get_all_flashes_in_a_step(energy_levels)
        flash = flash + len(flashed_coords)
    return flash


def flashing_octopuses_v2(energy_levels_raw):
    energy_levels = __transform_input(energy_levels_raw)
    step = 0
    sync_flash = False
    while not sync_flash:
        flashed_coords = __get_all_flashes_in_a_step(energy_levels)
        sync_flash = len(flashed_coords) == 100
        step = step + 1
    return step


def __get_all_flashes_in_a_step(energy_levels):
    flashed_coords = set()
    for x_coord, row in enumerate(energy_levels):
        for y_coord, coord_value in enumerate(row):
            __handle_coord(x_coord, y_coord, energy_levels, flashed_coords)
    return flashed_coords


def __transform_input(energy_levels_raw):
    energy_levels = list()
    for row in energy_levels_raw:
        row_of_ints = list()
        for char in list(row):
            row_of_ints.append(int(char))
        energy_levels.append(row_of_ints)
    return energy_levels


def __handle_coord(x_coord, y_coord, energy_levels, flashed_coords):
    increased_nrg, flashed = __increase_nrg_and_flash(x_coord, y_coord, energy_levels, flashed_coords)
    energy_levels[x_coord][y_coord] = increased_nrg
    if flashed:
        flashed_coords.add(str(x_coord) + str(y_coord))
        __do_adj(x_coord, y_coord, energy_levels, flashed_coords)


def __do_adj(x, y, energy_levels, flashed_coords):
    if x < 9:
        __handle_coord(x + 1, y, energy_levels, flashed_coords)
    if x < 9 and y < 9:
        __handle_coord(x + 1, y + 1, energy_levels, flashed_coords)
    if x < 9 and y > 0:
        __handle_coord(x + 1, y - 1, energy_levels, flashed_coords)
    if y < 9:
        __handle_coord(x, y + 1, energy_levels, flashed_coords)
    if y > 0:
        __handle_coord(x, y - 1, energy_levels, flashed_coords)
    if x > 0 and y > 0:
        __handle_coord(x - 1, y - 1, energy_levels, flashed_coords)
    if x > 0 and y < 9:
        __handle_coord(x - 1, y + 1, energy_levels, flashed_coords)
    if x > 0:
        __handle_coord(x - 1, y, energy_levels, flashed_coords)


def __increase_nrg_and_flash(x_coord, y_coord, energy_levels, flashed_coords):
    if energy_levels[x_coord][y_coord] == 0:
        if str(x_coord) + str(y_coord) in flashed_coords:
            return 0, False
        else:
            return 1, False
    if energy_levels[x_coord][y_coord] == 9:
        return 0, True
    return energy_levels[x_coord][y_coord] + 1, False


if __name__ == '__main__':
    m_headers = {
        'cookie': '<COOKIE HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/11/input", headers=m_headers).text.splitlines()
    file_input = open('energy_levels.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(flashing_octopuses_v1(url_input)))
    print("Part: 2 = " + str(flashing_octopuses_v2(url_input)))
