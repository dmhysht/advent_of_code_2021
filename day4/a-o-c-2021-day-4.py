# --- Day 4: Giant Squid ---
#
# https://adventofcode.com/2021/day/4

import requests
from collections import defaultdict


def giant_squid_bingo_part_1(bingo_input):
    bingo = __get_bingo_(bingo_input)
    for bingo_number in bingo['instructions']:
        winning_boards = __check_boards(bingo['boards'], bingo_number)
        if winning_boards:
            return __calculate_board_score(winning_boards[0], bingo_number)


def __check_boards(boards, bingo_number):
    won_boards = list()
    for board in boards:
        if bingo_number in board:
            won = __mark_and_return_if_won(board, bingo_number)
            if won:
                won_boards.append(won)
    if len(won_boards) > 0:
        for board in won_boards:
            boards.remove(board)
        return won_boards
    else:
        return None


def __calculate_board_score(winning_board, bingo_number):
    sum_of_unmarked = 0
    for num, status in winning_board.items():
        if status[len(status) - 1] != 'X':
            sum_of_unmarked = sum_of_unmarked + int(num)
    return sum_of_unmarked * int(bingo_number)


def __mark_and_return_if_won(board, bingo_number):
    board[bingo_number].append('X')
    row_to_check = board[bingo_number][0]
    col_to_check = board[bingo_number][1]
    row_marked = 0
    col_marked = 0
    for cell in board.values():
        if cell[0] == row_to_check and cell[len(cell) - 1] == 'X':
            row_marked = row_marked + 1
        if cell[1] == col_to_check and cell[len(cell) - 1] == 'X':
            col_marked = col_marked + 1
    if row_marked == 5 or col_marked == 5:
        return board
    return None


def giant_squid_bingo_part_2(bingo_input):
    bingo = __get_bingo_(bingo_input)
    winning_boards = dict()
    for bingo_number in bingo['instructions']:
        current_winners = __check_boards(bingo['boards'], bingo_number)
        if current_winners:
            for winning_board in current_winners:
                winning_boards[bingo_number] = winning_board
    final_winning_board_index = len(winning_boards) - 1
    list_of_boards = list(winning_boards.values())
    list_of_nums = list(winning_boards)
    return __calculate_board_score(list_of_boards[final_winning_board_index],
                                   list_of_nums[final_winning_board_index])


def __get_bingo_(bingo_input):
    bingo = defaultdict(list)
    read_instructions = False
    need_new_board = False
    row_pos = 0
    col_pos = 0
    for line in bingo_input:
        if not read_instructions:
            bingo['instructions'] = line.split(',')
            read_instructions = True
        else:
            if not line:
                need_new_board = True
                row_pos = 0
                col_pos = 0
                continue
            else:
                if need_new_board:
                    need_new_board = False
                    new_board = dict()
                    bingo['boards'].append(new_board)
                board = bingo['boards'][len(bingo['boards']) - 1]
                bingo_row = line.split(' ')
                for cell in bingo_row:
                    if not cell:
                        continue
                    board[cell] = [row_pos, col_pos]
                    col_pos = col_pos + 1
                row_pos = row_pos + 1
                col_pos = 0
    return bingo


if __name__ == '__main__':
    m_headers = {'cookie': ''}
    url_input = requests.get("https://adventofcode.com/2021/day/4/input", headers=m_headers).text.splitlines()
    file_input = open('bingo_instructions.txt', 'r').read().splitlines()
    print("Part: 1 = " + str(giant_squid_bingo_part_1(url_input)))
    print("Part: 2 = " + str(giant_squid_bingo_part_2(url_input)))


