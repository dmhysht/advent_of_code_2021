# --- Day 12: Passage Pathing ---
#
# https://adventofcode.com/2021/day/12

import requests


def cave_paths_v1(map_raw):
    caves_model = __build_caves_model(map_raw)
    valid_roads = list()
    __find_all_valid_paths("start", caves_model, "", valid_roads, 1, False)
    return len(valid_roads)


def cave_paths_v2(map_raw):
    caves_model = __build_caves_model(map_raw)
    valid_roads = list()
    __find_all_valid_paths("start", caves_model, "", valid_roads, 2, True)
    return len(valid_roads)


def __find_all_valid_paths(location, caves_model, current_road, valid_roads, allowed_to_visit, can_revisit_small_cave):
    if location == "end":
        current_road = current_road + location
        valid_roads.append(current_road)
    else:
        current_road = current_road + location + ","
        connected_caves = caves_model.get(location)
        if connected_caves:
            for connected_cave in connected_caves:
                if connected_cave == "start":
                    continue
                if connected_cave.isupper():
                    __find_all_valid_paths(connected_cave, caves_model, current_road, valid_roads, allowed_to_visit,
                                           can_revisit_small_cave)
                else:
                    times_visited = current_road.count(connected_cave)
                    if times_visited == 0:
                        __find_all_valid_paths(connected_cave, caves_model, current_road, valid_roads, allowed_to_visit,
                                               can_revisit_small_cave)
                    elif times_visited < allowed_to_visit and can_revisit_small_cave:
                        __find_all_valid_paths(connected_cave, caves_model, current_road, valid_roads, allowed_to_visit,
                                               False)


def __build_caves_model(map_raw):
    caves_dict = dict()
    for each in map_raw:
        split = each.split("-")
        if split[0] in caves_dict:
            caves_dict.get(split[0]).add(split[1])
        else:
            caves_dict[split[0]] = {split[1]}
    orphans = dict()
    for parent, children in caves_dict.items():
        for child in children:
            child_caves = caves_dict.get(child)
            if child_caves:
                if parent not in child_caves:
                    child_caves.add(parent)
            else:
                if child in orphans:
                    orphans.get(child).add(parent)
                else:
                    orphans[child] = {parent}
    caves_dict.update(orphans)
    return caves_dict


class Cave(object):
    def __init__(self, name):
        self.name = []


if __name__ == '__main__':
    m_headers = {
        'cookie': '<COOKIES HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/12/input", headers=m_headers).text.splitlines()
    file_input = open('cave_map.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(cave_paths_v1(url_input)))
    print("Part: 2 = " + str(cave_paths_v2(url_input)))
