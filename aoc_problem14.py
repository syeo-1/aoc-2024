from aoc_helper import *
from collections import namedtuple
from math import prod # note only can be used in python 3.8+
from functools import reduce
from operator import mul

point = namedtuple('Point', ['x', 'y'])
velocity = namedtuple('Velocity', ['x', 'y'])

def main():
    input_text = read_file_lines('input14.txt')
    layout = [['.']*101 for _ in range(103)]
    # layout = [['.']*11 for _ in range(7)]
    # print(layout)
    # for thing in layout:
    #     print(''.join(thing))

    processed_robot_data = []

    for raw_robot_data in input_text:
        separated_data = raw_robot_data.split()
        single_unprocessed_robot_point = separated_data[0].split('=')[1].split(',')
        processed_robot_point = point(int(single_unprocessed_robot_point[0]), int(single_unprocessed_robot_point[1]))

        single_unprocessed_robot_velocity = separated_data[1].split('=')[1].split(',')
        processed_robot_velocity = velocity(int(single_unprocessed_robot_velocity[0]), int(single_unprocessed_robot_velocity[1]))

        processed_robot_data.append([processed_robot_point, processed_robot_velocity])
        # print(processed_robot_data)
        # break

    # print(processed_robot_data)
    # print('===========')

    # processed_robot_data = [[point(x=2, y=4), velocity(x=2, y=-3)]]
    for _ in range(100):
        for i, robot_data in enumerate(processed_robot_data):
            cur_point = robot_data[0]
            cur_velocity = robot_data[1]

            # calculate new x and y values
            new_x = cur_point.x + cur_velocity.x
            new_y = cur_point.y + cur_velocity.y

            if new_x < 0:
                new_x = len(layout[0]) + new_x
            elif new_x >= len(layout[0]):
                new_x = new_x - len(layout[0])

            if new_y < 0:
                new_y = len(layout) + new_y
            elif new_y >= len(layout):
                new_y = new_y - len(layout)
            
            new_point = point(x = new_x, y = new_y)

            processed_robot_data[i] = [new_point, cur_velocity]
        
        # print(processed_robot_data)
        # print('===========')

        # get the quadrant values

        midx = len(layout[0])//2
        midy = len(layout)//2

        q_count = [0]*4

        for robot_data in processed_robot_data:
            cur_point = robot_data[0]

            curx = cur_point.x
            cury = cur_point.y

            if 0 <= curx < midx and 0 <= cury < midy: # q1
                q_count[0] += 1
            elif midx < curx < len(layout[0]) and 0 <= cury < midy: # q2
                q_count[1] += 1
            elif 0 <= curx < midx and midy < cury < len(layout): # q3
                q_count[2] += 1
            elif midx < curx < len(layout[0]) and midy < cury < len(layout): # q4
                q_count[3] += 1

    # if python 3.8+ only
    print(prod(q_count))

    # python <3.8
    print(reduce(mul, q_count, 1))

    # print(input_text)

if __name__ == '__main__':
    main()