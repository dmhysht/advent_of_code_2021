# --- Day 7: The Treachery of Whales  ---
#
# https://adventofcode.com/2021/day/7

import requests

throttle_map = dict()


def crab_attack_part_1(crab_position):
    return __crab_attack(crab_position, __fuel_cost_v1)


def crab_attack_part_2(crab_position):
    return __crab_attack(crab_position, __fuel_cost_v2)


def __crab_attack(crab_position, fuel_cost):
    min_max = __find_min_max_possible_location(crab_position)
    __fill_throttle_map(min_max[1])
    min_fuel_used = None
    for pos_attempt in range(min_max[0], min_max[1]):
        fuel_used = 0
        for i in range(len(crab_position)):
            fuel_used = fuel_used + fuel_cost(crab_position[i], pos_attempt)
        if min_fuel_used is None:
            min_fuel_used = fuel_used
            continue
        if fuel_used < min_fuel_used:
            min_fuel_used = fuel_used
    return min_fuel_used


def __fill_throttle_map(max_pos):
    throttle_map[0] = 0
    for i in range(1, int(max_pos) + 1):
        throttle_map[i] = throttle_map[i - 1] + i


def __fuel_cost_v1(crab_position, pos_attempt):
    return abs((int(crab_position) - pos_attempt))


def __fuel_cost_v2(crab_position, pos_attempt):
    return throttle_map[abs((int(crab_position) - pos_attempt))]


def __find_min_max_possible_location(crab_position):
    min_pos = int(crab_position[0])
    max_pos = int(crab_position[0])
    for pos in crab_position:
        if int(pos) > max_pos:
            max_pos = int(pos)
        if int(pos) < min_pos:
            min_pos = int(pos)
    return [min_pos, max_pos]


if __name__ == '__main__':
    m_headers = {'cookie': '<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/7/input", headers=m_headers).text.split(",")
    file_input = open('position.txt', 'r').read().split(",")
    print("Part: 1 = " + str(crab_attack_part_1(url_input)))
    print("Part: 2 = " + str(crab_attack_part_2(url_input)))


