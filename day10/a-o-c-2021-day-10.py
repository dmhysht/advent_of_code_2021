# --- Day 10: Syntax Scoring ---
#
# https://adventofcode.com/2021/day/10

import requests

openers = {'(', '{', '<', '['}
closers = {')', '}', '>', ']'}

o2c = {'(': ')',
       '{': '}',
       '<': '>',
       '[': ']'}
c2o = {')': '(',
       '}': '{',
       '>': '<',
       ']': '['}


def syntax_error_score_v1(syntax_lines):
    score = 0
    for line in syntax_lines:
        score = score + __get_corrupted_score(__get_corrupted_bracket(line))
    return score


def syntax_error_score_v2(syntax_lines):
    scores = list()
    for line in syntax_lines:
        if __get_corrupted_bracket(line) is None:
            scores.append(__get_autocomplete_score(__complete_line(line)))
    scores.sort()
    return scores[int(len(scores) / 2)]


def __complete_line(line):
    stack = []
    for bracket in line:
        if c2o.get(peek_stack(stack)) == o2c.get(bracket):
            stack.pop()
        else:
            stack.append(bracket)
    completion_chunk = ""
    while stack:
        completion_chunk = completion_chunk + o2c.get(peek_stack(stack))
        stack.pop()
    return completion_chunk


def __get_autocomplete_score(completion_chunk):
    points = {')': 1, '}': 3, '>': 4, ']': 2}
    score = 0
    for bracket in completion_chunk:
        score = score * 5 + points.get(bracket)

    return score


def __get_corrupted_score(bracket):
    points = {')': 3, '}': 1197, '>': 25137, ']': 57}
    if bracket:
        return points[bracket]
    else:
        return 0


def __get_corrupted_bracket(line):
    stack = []
    for bracket in line:
        if bracket in openers:
            stack.append(bracket)
        else:
            if peek_stack(stack) == c2o.get(bracket):
                stack.pop()
            else:
                return bracket
    return None


def peek_stack(stack):
    if stack:
        return stack[-1]
    else:
        return None


if __name__ == '__main__':
    m_headers = {
        'cookie': '<TOKEN HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/10/input", headers=m_headers).text.splitlines()
    file_input = open('syntax.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(syntax_error_score_v1(url_input)))
    print("Part: 2 = " + str(syntax_error_score_v2(url_input)))
