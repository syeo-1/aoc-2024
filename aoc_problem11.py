from aoc_helper import *

from math import log10
from functools import cache

def rule2(stone):
    stones = list(str(stone))

    stone_len = len(stones)//2
    # print(stones)

    return [int(''.join(stones[:stone_len])), int(''.join(stones[stone_len:]))]

ten_exps = [pow(10, i) for i in range(20)]


@cache
def rule2_efficient(stone):
    num_digits = int(log10(stone))+1
    new_stone_size = num_digits//2

    # back half will be stone % 10^new_stone_size
    # eg. 1234 % 100 = 34
    back = stone % ten_exps[new_stone_size]

    # front half will be stone // 10^new_stone_size
    # eg. 1234 // 100 = 12
    front = stone // ten_exps[new_stone_size]

    return (front, back)



def main():
    initial_input = read_file_lines('input11_sample.txt')
    # print(initial_input)
    current_stones = [int(s) for s in initial_input[0].split()]
    print(current_stones)

    # for _ in range(75):
    #     new_stones = []
    #     for stone in current_stones:
    #         if stone == 0:
    #             new_stones.append(1)
    #         elif len(str(stone))%2 == 0:
    #             new_stones.extend(rule2(stone))
    #         else:
    #             new_stones.append(stone*2024)

    #     current_stones = new_stones
    #     print(current_stones)

    for _ in range(75):
        new_stones = []
        for i, stone in enumerate(current_stones):
            if stone == 0:
                # new_stones.append(1)
                current_stones[i] = 1
            elif (int(log10(stone))+1)%2 == 0:
                # set values
                front, back = rule2_efficient(stone)
                current_stones[i] = front

                current_stones = current_stones[:i+1] + [back] + current_stones[i+1:]

            else:
                # new_stones.append(stone*2024)
                current_stones[i] = current_stones[i] * 2024

            # print(current_stones)
        
        # break

        # current_stones = new_stones
        # print(current_stones)
    
    print(len(current_stones))
        


if __name__ == '__main__':
    main()