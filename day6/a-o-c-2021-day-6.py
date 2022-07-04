# --- Day 6: Lanternfish  ---
#
# https://adventofcode.com/2021/day/6

import requests
from collections import defaultdict


# simple, works for small  number of days only
def fancy_fishes_part_1(fish_list):
    for day in range(80):
        next_day_fishes = list()
        for fish in fish_list:
            if fish == 0:
                next_day_fishes.append(8)
                next_day_fishes.append(6)
            else:
                next_day_fishes.append(int(fish) - 1)
        fish_list = next_day_fishes
    return len(fish_list)


def fancy_fishes_part_2(fish_list):
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fish_list:
        nums[int(fish)] = nums[int(fish)] + 1

    for day in range(256):
        mem1 = nums[8]
        for num_check in range(8, -1, -1):
            if num_check != 0:
                mem2 = nums[num_check - 1]
                nums[num_check - 1] = mem1
                mem1 = mem2
            else:
                nums[6] = nums[6] + mem1
                nums[8] = mem1

    count = 0
    for fish_count in nums:
        count = count + fish_count

    return count


if __name__ == '__main__':
    m_headers = {'cookie': '<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/6/input", headers=m_headers).text.split(",")
    file_input = open('fishes_input.txt', 'r').read().split(",")
    print("Part: 1 = " + str(fancy_fishes_part_1(url_input)))
    print("Part: 2 = " + str(fancy_fishes_part_2(url_input)))


