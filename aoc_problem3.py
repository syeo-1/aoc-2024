from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
)

import re

def main():
    file_lines = read_file_lines('input3.txt')
    # lines = split_file_line_contents_whitespace(file_lines, 'str')
    # print(lines)

    # mul_pattern_p1 = r"mul\((\d{1,3}),(\d{1,3})\)"
    mul_pattern_p2 = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"


    ##### PART 1 START #####
    # total = 0
    # for line in file_lines:
    #     matches = re.findall(mul_pattern_p1, line)
    #     for match in matches:
    #         total += int(match[0])*int(match[1])

    # print(total)
    ##### PART 1 END #####

    ##### PART 2 START #####
    total = 0
    mul_active = True
    for line in file_lines:
        matches = re.findall(mul_pattern_p2, line)
        for match in matches:
            if 'don\'t()' in match:
                mul_active = False
            elif 'do()' in match:
                mul_active = True
            
            if mul_active and 'don\'t()' not in match and 'do()' not in match:
                total += int(match[0])*int(match[1])
    print(total)

    ##### PART 2 END #####

if __name__ == '__main__':
    main()