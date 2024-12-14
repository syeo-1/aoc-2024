from aoc_helper import *
from collections import deque

def inbounds(coord, row_bound, col_bound):
    row = coord[0]
    col = coord[1]

    if 0 <= row < row_bound and 0 <= col < col_bound:
        return True
    return False

def count_nine_paths(topographical_map, zero_location):

    unique_nine_locations = set()
    location_deque = deque()
    explored = set()

    location_deque.append(tuple(zero_location))

    # perform BFS
    # used pseudocode from this as reference: https://en.wikipedia.org/wiki/Breadth-first_search
    while location_deque:
        to_check = location_deque.popleft()
        
        left = (to_check[0], to_check[1]-1)
        right = (to_check[0], to_check[1]+1)
        up = (to_check[0]-1, to_check[1])
        down = (to_check[0]+1, to_check[1])

        

        if topographical_map[to_check[0]][to_check[1]] == 9:
            unique_nine_locations.add(to_check)

        if inbounds(left, len(topographical_map), len(topographical_map[0])) and topographical_map[left[0]][left[1]] == topographical_map[to_check[0]][to_check[1]] + 1 and left not in explored:
            location_deque.append(left)
            explored.add(left)
        if inbounds(right, len(topographical_map), len(topographical_map[0])) and topographical_map[right[0]][right[1]] == topographical_map[to_check[0]][to_check[1]] + 1 and right not in explored:
            location_deque.append(right)
            explored.add(right)
        if inbounds(up, len(topographical_map), len(topographical_map[0])) and topographical_map[up[0]][up[1]] == topographical_map[to_check[0]][to_check[1]] + 1 and up not in explored:
            location_deque.append(up)
            explored.add(up)
        if inbounds(down, len(topographical_map), len(topographical_map[0])) and topographical_map[down[0]][down[1]] == topographical_map[to_check[0]][to_check[1]] + 1 and down not in explored:
            location_deque.append(down)
            explored.add(down)
        
        # print('blah')

    # return unique_nine_locations
    # print(unique_nine_locations)

    return len(unique_nine_locations)


def main():
    initial_input = read_file_lines('input10.txt')
    # print(initial_input)

    processed_input = [list(s) for s in initial_input]
    for i in range(len(processed_input)):
        for j in range(len(processed_input[0])):
            processed_input[i][j] = int(processed_input[i][j])
    
    # print(processed_input)
    
    # find locations of all zeros first
    zero_locations = []
    for i in range(len(processed_input)):
        for j in range(len(processed_input[0])):
            if processed_input[i][j] == 0:
                zero_locations.append([i, j])

    # print(zero_locations)
    total_trailhead_score = 0
    for location in zero_locations:
        total_trailhead_score += count_nine_paths(processed_input, location)

    print(total_trailhead_score)
        

if __name__ == '__main__':
    main()