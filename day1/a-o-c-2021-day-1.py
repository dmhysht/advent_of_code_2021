# --- Day 1: Sonar Sweep ---
#
# https://adventofcode.com/2021/day/1

import requests


def count_increases_part_1(depth_position):
    count = 0
    prev = int(depth_position[0])
    for depth in depth_position:
        if int(depth) > prev:
            count = count + 1
        prev = int(depth)

    return count


def count_increases_part_2(depth_position):
    count = 0
    prev = int(depth_position[0]) + int(depth_position[1]) + int(depth_position[2])
    for i in range(len(depth_position)):
        if __is_window_available(i, len(depth_position), 3):
            current_window = int(depth_position[i]) + int(depth_position[i + 1]) + int(depth_position[i + 2])
            if current_window > prev:
                count = count + 1
            prev = current_window
        else:
            break
    return count


def __is_window_available(current_pos, total_elements, window_size):
    for i in range(window_size):
        if current_pos + i <= total_elements - 1:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    m_headers = {'cookie':'<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/1/input", headers=m_headers).text.splitlines()
    file_input = open('report.txt', 'r').read().splitlines()
    print(count_increases_part_1(url_input))
    print(count_increases_part_2(url_input))


