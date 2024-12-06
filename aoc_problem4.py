from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix
)

import numpy as np

# def count_num_substring_occurances(substr, str):
#     # given substr, count number of occurances of the substring in str

#     substr_count = 0
#     for i in range(len(str)-len(substr)):
#         if str[i:i+len(substr)] == substr:
#             substr_count += 1
#     return substr_count

def diag_count(np_matrix):

    substr_count = 0
    for i in range(len(np_matrix)):
        if i == 0:
            k_diag = np.diag(np_matrix)
            print(''.join(k_diag))
            substr_count += ''.join(k_diag).count('XMAS')
            substr_count += ''.join(k_diag).count('SAMX')
        else:
            k_diag = np.diag(np_matrix, i)
            k_neg_diag = np.diag(np_matrix, -i)
            print('===')
            print(''.join(k_diag))
            print(''.join(k_neg_diag))
            # exit(0)


            substr_count += ''.join(k_diag).count('XMAS')
            substr_count += ''.join(k_diag).count('SAMX')
            substr_count += ''.join(k_neg_diag).count('XMAS')
            substr_count += ''.join(k_neg_diag).count('SAMX')

    return substr_count

def main():
    file_lines = read_file_lines('input4.txt')

    ##### PART 1 START #####

    # overall_substr_count = 0

    # # horizontal check
    # for line in file_lines:
    #     overall_substr_count += line.count('XMAS')
    #     overall_substr_count += line.count('SAMX')
    # print(overall_substr_count)

    # # exit(0)

    # # vertical check
    # vertical_mat_initial = [list(line) for line in file_lines]
    # # print(vertical_mat_initial)
    # transposed_file_lines = transpose_matrix(vertical_mat_initial)
    # vertical_mat_transformed = [''.join(line) for line in transposed_file_lines]
    # # print(vertical_mat_transformed[0])
    # for line in vertical_mat_transformed:
    #     overall_substr_count += line.count('XMAS')
    #     overall_substr_count += line.count('SAMX')
    
    # print(overall_substr_count)
    # # exit(0)

    # # diagonal check. use numpy. First convert to a numpy nested array
    # np_matrix = np.array([np.array(ls) for ls in vertical_mat_initial])
    # overall_substr_count += diag_count(np_matrix)
    # print(overall_substr_count)
            
    # # first check normal diagonals, then flip and check again!
    # yaxis_flipped_mat = np.fliplr(np_matrix)
    # overall_substr_count += diag_count(yaxis_flipped_mat)
    # print(overall_substr_count)
    ##### PART 1 END #####

    ##### PART 2 START #####
    vertical_mat_initial = [list(line) for line in file_lines]
    np_matrix = np.array([np.array(ls) for ls in vertical_mat_initial])
    print(np_matrix)

    # I'm just gonna do it the brute force easy way with numpy

    # use sliding window and just look for the hardcoded values in the numpy array

    
    ##### PART 2 END #####





    

if __name__ == '__main__':
    main()