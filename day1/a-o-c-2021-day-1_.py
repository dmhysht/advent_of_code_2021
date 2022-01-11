import requests


def count_increases(increases):
    count = 0
    prev = increases[0]
    for depth in increases:
        if depth > prev:
            count = count + 1
        prev = depth
    return count


if __name__ == '__main__':
    m_headers = {'cookie':''}
    url_input = requests.get("https://adventofcode.com/2021/day/1/input", headers=m_headers).text.split("\n")
    file_input = open('report.txt', 'r').readlines()
    print(count_increases(url_input))


