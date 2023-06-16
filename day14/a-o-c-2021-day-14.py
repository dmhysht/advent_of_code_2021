# --- Day 14: Extended Polymerization ---
#
# https://adventofcode.com/2021/day/14

import requests


def polymerization_v1(insertion_rules):
    pairs_count, count_map, rules = __extract_data(insertion_rules)
    count_map = __run_polymerization(pairs_count, count_map, rules, 10)
    return __delta_of_ho_and_lo(count_map)


def polymerization_v2(insertion_rules):
    pairs_count, count_map, rules = __extract_data(insertion_rules)
    count_map = __run_polymerization(pairs_count, count_map, rules, 40)
    return __delta_of_ho_and_lo(count_map)


def __extract_data(insertion_rules_raw):
    template = insertion_rules_raw[0]
    count_map = __get_initial_count(template)
    pairs_count = __get_initial_pairs_count(template)
    rules = __get_rules(insertion_rules_raw)
    return pairs_count, count_map, rules


def __get_initial_count(template):
    count_map = dict()
    for i in range(len(template)):
        count_map[template[i]] = count_map.get(template[i], 0) + 1
    return count_map


def __get_initial_pairs_count(template):
    pairs_count = dict()
    template_idx = 0
    while template_idx < len(template) - 1:
        pair = template[template_idx] + template[template_idx + 1]
        pairs_count[pair] = pairs_count.get(pair, 0) + 1
        template_idx += 1
    return pairs_count


def __get_rules(insertion_rules_raw):
    rules = dict()
    idx = 2
    while idx < len(insertion_rules_raw):
        rules[insertion_rules_raw[idx].split(' -> ')[0]] = insertion_rules_raw[idx].split(' -> ')[1]
        idx += 1
    return rules


def __run_polymerization(pairs_count, count_map, rules, number_of_runs):
    idx = 0
    while idx < number_of_runs:
        pairs_count = __polymerization_run(pairs_count, rules, count_map)
        idx += 1
    return count_map



def __polymerization_run(pairs, rules, count_map):
    new_pairs = dict()
    for pair in pairs.keys():
        insertion = rules.get(pair)
        new_pairs[pair[0] + insertion] = new_pairs.get(pair[0] + insertion, 0) + pairs.get(pair)
        new_pairs[insertion + pair[1]] = new_pairs.get(insertion + pair[1], 0) + pairs.get(pair)
        count_map[insertion] = count_map.get(insertion, 0) + pairs.get(pair)
    return new_pairs


def __delta_of_ho_and_lo(count_map):
    seed = list(count_map.values())[0]
    ho = seed
    lo = seed
    for count in count_map.values():
        if count > ho:
            ho = count
        if count < lo:
            lo = count
    return ho - lo


if __name__ == '__main__':
    m_headers = {
        'cookie': '<COOKIE HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/14/input", headers=m_headers).text.splitlines()
    file_input = open('insertion_rules.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(polymerization_v1(url_input)))
    print("Part: 2 = " + str(polymerization_v2(url_input)))
