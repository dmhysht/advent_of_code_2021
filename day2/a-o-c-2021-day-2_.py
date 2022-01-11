
import requests


def calculate_position_part_1(course):
    horizontal_pos = 0
    depth = 0
    for instruction in course:
        if "forward" in instruction:
            horizontal_pos = horizontal_pos + int(instruction.split(" ")[1])
        elif "up" in instruction:
            depth = depth - int(instruction.split(" ")[1])
        elif "down" in instruction:
            depth = depth + int(instruction.split(" ")[1])

    return horizontal_pos * depth


def calculate_position_part_2(course):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for instruction in course:
        if "forward" in instruction:
            horizontal_pos = horizontal_pos + int(instruction.split(" ")[1])
            depth = depth + (aim * int(instruction.split(" ")[1]))
        elif "up" in instruction:
            aim = aim - int(instruction.split(" ")[1])
        elif "down" in instruction:
            aim = aim + int(instruction.split(" ")[1])

    return horizontal_pos * depth


if __name__ == '__main__':
    m_headers = {'cookie': '<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/2/input", headers=m_headers).text.split("\n")
    file_input = open('course.txt', 'r').readlines()
    print("Part: 1 =" + str(calculate_position_part_1(url_input)))
    print("Part: 2 =" + str(calculate_position_part_2(url_input)))


