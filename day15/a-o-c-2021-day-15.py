# --- Day 15: Chiton ---
#
# https://adventofcode.com/2021/day/15
import sys
import time
from queue import PriorityQueue

import requests


def evaluate_risk_v1(risk_map):
    rows, cols = (len(risk_map), len(risk_map[0]))
    visited = [[0 for x in range(cols)] for y in range(rows)]
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        item = pq.get()
        y = item[1][0]
        x = item[1][1]
        if visited[y][x] != 0:
            continue
        curr = item[0]
        if y == len(risk_map) - 1 and x == len(risk_map[0]) - 1:
            return curr
        visited[y][x] = curr

        if y < len(risk_map) - 1:
            pq.put((curr + int(risk_map[y+1][x]), (y+1, x)))
        if x < len(risk_map[0]) - 1:
            pq.put((curr + int(risk_map[y][x+1]), (y, x+1)))
        if y > 0:
            pq.put((curr + int(risk_map[y-1][x]), (y-1, x)))
        if x > 0:
            pq.put((curr + int(risk_map[y][x-1]), (y, x-1)))
    # should never get here
    return sys.maxsize


def evaluate_risk_v2(risk_map):
    rows, cols = (len(risk_map), len(risk_map[0]))
    row = 0
    col = 0
    enlarged = list()
    while row < rows * 5:
        enlarged.append(list())
        row_inc = int(row / len(risk_map))
        while col < cols * 5:
            col_inc = int(col / len(risk_map[0]))
            idx_x = col % len(risk_map[0])
            idx_y = row % len(risk_map)
            val = int(risk_map[idx_y][idx_x])
            final_val = __rotate_val(val + row_inc + col_inc)
            enlarged[row].append(final_val)
            col += 1
        col = 0
        row += 1
    return evaluate_risk_v1(enlarged)


def __rotate_val(val):
    while val >= 10:
        val -= 9
    return val


if __name__ == '__main__':
    m_headers = {
        'cookie': '<COOKIE HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/15/input", headers=m_headers).text.splitlines()
    file_input = open('risk_level_map.txt', 'r').read().splitlines()
    start = time.time() * 1000
    print("Part: 1 = " + str(evaluate_risk_v1(url_input)))
    print("Took: " + str(time.time() * 1000 - start))
    start = time.time() * 1000
    print("Part: 2 = " + str(evaluate_risk_v2(url_input)))
    print("Took: " + str(time.time() * 1000 - start))
