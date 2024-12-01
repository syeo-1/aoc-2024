from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix
)

from collections import Counter


def main():
    file_lines = read_file_lines('input1.txt')
    processed_file_lines = split_file_line_contents_whitespace(file_lines, 'int')

    # matrix transpose the file contents so easier to work with
    transposed_file_lines = transpose_matrix(processed_file_lines)

    # ###### PART 1 START #####
    # # sort the sublists in-place
    # for i in range(len(transposed_file_lines)):
    #     transposed_file_lines[i].sort()
    
    # # compute distances and sum
    # result = 0
    # # lengths are same for both lists, so doesn't matter
    # for i in range(len(transposed_file_lines[0])):
    #     result += abs(transposed_file_lines[0][i]-transposed_file_lines[1][i])
    
    # # part 1 done!
    # # print(result)
    # ###### PART 1 END #####


    ##### PART 2 START #####
    result = 0
    list2_counter = Counter(transposed_file_lines[1])
    for num in transposed_file_lines[0]:
        if num in list2_counter:
            result += num * list2_counter[num]
    print(result)
    ##### PART 2 END #####

if __name__ == '__main__':
    main()