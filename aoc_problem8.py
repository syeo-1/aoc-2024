from aoc_helper import *
from collections import defaultdict
from itertools import permutations

def inmap_check(antinode_locations, rowbound, colbound):
    result = []

    for location in antinode_locations:
        if 0 <= location[0] < rowbound and 0 <= location[1] < colbound:
            result.append(location)

    return result




def get_antinode_locations(antenna_pair):
    # given an antenna pair, find the locations they should be at
    # get the ansolute coordinate distance the antennas are from each other
    coord1 = antenna_pair[0]
    coord2 = antenna_pair[1]
    # row, col. from c1 to c2
    antenna_distance = [coord1[0]-coord2[0], coord1[1]-coord2[1]]

    # antinode for antenna1
    # just travel the opposite direction of the distance just found to get it
    c1_antinode = [coord1[0]+antenna_distance[0], coord1[1]+antenna_distance[1]]
    c2_antinode = [coord2[0]-antenna_distance[0], coord2[1]-antenna_distance[1]]
    # print(antenna_distance)
    # print(c1_antinode)
    # print(c2_antinode)
    
    return [c1_antinode, c2_antinode]



def main():
    initial_input = read_file_lines('input8.txt')
    processed_map = [list(s) for s in initial_input]
    antinode_map = [['.']*len(processed_map[0]) for _ in range(len(processed_map))]
    # print(antinode_map)
    # print(processed_map)

    # get all locations of antenna
    # since a non-dot represents a location, just store the coordinates of the antenna
    antenna_locations = defaultdict(list)
    for i in range(len(processed_map)):
        for j in range(len(processed_map[0])):
            if processed_map[i][j] != '.':
                antenna_locations[processed_map[i][j]].append([i, j])

    # print(antenna_locations)
    overall_antinode_locations = []
    for antenna_type in antenna_locations:
        antenna_pair_permutations = permutations(antenna_locations[antenna_type], 2)
        # print(antenna_pair_permutations)
        for perm in antenna_pair_permutations:
            antinode_locations = get_antinode_locations(perm)
            inmap_antinode_locations = inmap_check(antinode_locations, len(processed_map), len(processed_map[0]))
            # print(perm)
            # print(inmap_antinode_locations)
            overall_antinode_locations.extend(inmap_antinode_locations)
            # print(overall_antinode_locations)
        #     break
        # break
    
    for location in overall_antinode_locations:
        antinode_map[location[0]][location[1]] = '#'

    antinode_count = 0
    for r in antinode_map:
        for c in r:
            if c == '#':
                antinode_count += 1

    print(antinode_count)

    # for thing in antinode_map:
    #     print(''.join(thing))
    




if __name__ == '__main__':
    main()