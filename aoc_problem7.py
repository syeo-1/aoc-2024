from aoc_helper import *
from itertools import product

def generate_operation_strings(d, n, ops):
    for i in range(n):
        for op in ops:
            pass


def main():
    initial_input = read_file_lines('input7.txt')
    print(initial_input)

    parsed_input = [line.split(': ') for line  in initial_input]
    start = {}
    for l in parsed_input:
        start[int(l[0])] = [int(num) for num in l[1].split()]

    
    
    working_keys = []
    for k, v in start.items():
        # print(k)
        # print(v)
        # https://stackoverflow.com/questions/30672738/python-how-to-generate-permutations-of-size-greater-than-the-number-of-list-el
        operation_permutation = list(product(['*','+'], repeat=len(v)-1))

        for op_list in operation_permutation:
            temp_sum = v[0]
            for i, op in enumerate(op_list):
                if op == '*':
                    temp_sum *= v[i+1]
                elif op == '+':
                    temp_sum += v[i+1]

            # print(temp_sum)
            if temp_sum == k:
                working_keys.append(k)
                break

    print(sum(working_keys))

        # print(operation_permutation)
        # break



if __name__ == '__main__':
    main()