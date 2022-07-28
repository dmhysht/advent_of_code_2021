# --- Day 8: Seven Segment Search  ---
#
# https://adventofcode.com/2021/day/8

import requests


def signal_decoder_v1(signals):
    found = 0
    for signal in signals:
        if len(signal) != 0:
            for second_part in signal.split(" | ")[1].split(" "):
                if len(second_part) == 2 or len(second_part) == 4 or len(second_part) == 3 or len(second_part) == 7:
                    found = found + 1
    return found


def signal_decoder_v2(signals):
    total = 0
    for signal in signals:
        if len(signal) != 0:
            first_part = signal.split(" | ")[0]
            second_part = signal.split(" | ")[1]
            decoder = __gen_decoder(first_part)
            number = ''
            for code in second_part.split(" "):
                number = number + __get_number_from_decoder(decoder, code)
            total = total + int(number)

    return total


def __get_number_from_decoder(decoder, code):
    for decode in decoder:
        if len(decode) != len(code):
            continue
        found = True
        for element in code:
            if element not in decode:
                found = False
                break
        if found:
            return decoder[decode]


def __gen_decoder(first_part):
    encoder = dict()
    decoder = dict()
    __decode_1478(first_part, encoder, decoder)
    __decode_023569(first_part, encoder, decoder)
    return decoder


def __decode_1478(first_part, encoder, decoder):
    for code in first_part.split(" "):
        if len(code) == 2:
            encoder[1] = code
            decoder[code] = '1'
        if len(code) == 3:
            decoder[code] = '7'
        if len(code) == 4:
            encoder[4] = code
            decoder[code] = '4'
        if len(code) == 7:
            decoder[code] = '8'


def __decode_023569(first_part, encoder, decoder):
    for code in first_part.split(" "):
        if len(code) == 5:  # means could be 2, 5 or 3
            # 3 contains both segments of 1
            if __is_three(code, encoder[1]):
                decoder[code] = '3'
            # 5 contains 3 segments of the 4 and only one of the segments of the 1
            elif __is_five(code, encoder[4], encoder[1]):
                decoder[code] = '5'
            else:
                # else 2 is the last code that has 5 characters
                decoder[code] = '2'
        elif len(code) == 6:  # means can be 6, 9 or 0
            # 6 contains only 1 segment but not the other from the 1
            if __is_six(code, encoder[1]):
                decoder[code] = '6'
            # 9 contains all segments of 4
            elif __is_nine(code, encoder[4]):
                decoder[code] = '9'
            else:
                # else 0 is the last deducible code that has 6 characters
                decoder[code] = '0'


def __is_three(code, segments_of_one):
    return segments_of_one[0] in code and segments_of_one[1] in code


def __is_five(code, segments_of_four, segments_of_one):
    segments_found = 0
    for segment in segments_of_four:
        if segment in code:
            segments_found = segments_found + 1
    return segments_found == 3 and not __is_three(code, segments_of_one)


def __is_six(code, segments_of_one):
    return (segments_of_one[0] in code and segments_of_one[1] not in code)\
           or (segments_of_one[0] not in code and segments_of_one[1] in code)


def __is_nine(code, segments_of_four):
    all_segments = True
    for segment in segments_of_four:
        if segment not in code:
            all_segments = False
            break
    return all_segments


if __name__ == '__main__':
    m_headers = {
        'cookie': '<INSERT HERE>'}
    url_input = requests.get("https://adventofcode.com/2021/day/8/input", headers=m_headers).text.split("\n")
    file_input = open('output.txt', 'r').read().split("\n")
    print("Part: 1 = " + str(signal_decoder_v1(url_input)))
    print("Part: 2 = " + str(signal_decoder_v2(url_input)))
