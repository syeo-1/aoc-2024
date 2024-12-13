from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix
)

dirn_map = {
    'up': '^',
    'right': '>',
    'down': 'V',
    'left': '<'
}

def get_starting_position(patrol_layout):
    
    for i, l in enumerate(patrol_layout):
        for j, c in enumerate(l):
            if c == '^':
                return [i, j]
            
def move_guard(direction):
    # given the direction that the guard should move in
    # move the guard one space in the given direction
    pass

def main():
    initial_input = read_file_lines('input6.txt')
    patrol_layout = [list(s) for s in initial_input]
    map_copy = [['.']*len(patrol_layout[0]) for i in range(len(patrol_layout))]
    guard_position = get_starting_position(patrol_layout)
    print(guard_position)
    print(map_copy)

    # can mark the map_copy
    g_row = guard_position[0]
    g_col = guard_position[1]
    guard_orientation = patrol_layout[g_row][g_col]
    orientation_change = False
    print(guard_orientation)
    # print([g_row, g_col])
    while 0 <= g_row < len(patrol_layout) and 0 <= g_col < len(patrol_layout[0]):
        
        if orientation_change and patrol_layout[g_row][g_col] == '.':
            # check if current square is marked, if not mark it
            patrol_layout[g_row][g_col] = 'X'
            orientation_change = False

        match guard_orientation:
            case '^':
                # try and move up
                # check if you can move up
                if g_row - 1 < 0:
                    patrol_layout[g_row][g_col] = 'X'
                    break
                elif g_row - 1 >= 0 and patrol_layout[g_row-1][g_col] == '.':
                    # inbounds of row moving up
                    # print('b lah')
                    patrol_layout[g_row][g_col] = 'X'
                    g_row -= 1
                    # print([g_row, g_col])
                elif g_row - 1 >= 0 and patrol_layout[g_row-1][g_col] == '#':
                    # print('awefaweg')
                    guard_orientation = '>'
                    # need to mark and move
                    orientation_change = True
                    patrol_layout[g_row][g_col] = 'X'
                    g_col += 1
                    # print([g_row, g_col])
                    # print([g_row, g_col])
                elif g_row - 1 >= 0 and patrol_layout[g_row-1][g_col] == 'X':
                    patrol_layout[g_row][g_col] = 'X'
                    g_row -= 1
                    # print([g_row, g_col])
            case '>':
                if g_col + 1 >= len(patrol_layout[0]):
                    patrol_layout[g_row][g_col] = 'X'
                    break
                elif g_col + 1 < len(patrol_layout[0]) and patrol_layout[g_row][g_col+1] == '.':
                    # inbounds of column moving right
                    patrol_layout[g_row][g_col] = 'X'
                    g_col += 1
                    # print([g_row, g_col])
                elif g_col + 1 < len(patrol_layout[0]) and patrol_layout[g_row][g_col+1] == '#':
                    guard_orientation = 'V'
                    orientation_change = True
                    patrol_layout[g_row][g_col] = 'X'
                    g_row += 1

                    # print([g_row, g_col])
                elif g_col + 1 < len(patrol_layout[0]) and patrol_layout[g_row][g_col+1] == 'X':
                    patrol_layout[g_row][g_col] = 'X'
                    g_col += 1
                    # print([g_row, g_col])
            case 'V':
                if g_row + 1 >= len(patrol_layout):
                    patrol_layout[g_row][g_col] = 'X'
                    break
                elif g_row + 1 < len(patrol_layout) and patrol_layout[g_row+1][g_col] == '.':
                    # inbounds of row moving down
                    patrol_layout[g_row][g_col] = 'X'
                    g_row += 1
                    # print([g_row, g_col])
                elif g_row + 1 < len(patrol_layout) and patrol_layout[g_row+1][g_col] == '#':
                    guard_orientation = '<'
                    orientation_change = True
                    patrol_layout[g_row][g_col] = 'X'
                    g_col -= 1
                    # print([g_row, g_col])
                elif g_row + 1 < len(patrol_layout) and patrol_layout[g_row+1][g_col] == 'X':
                    patrol_layout[g_row][g_col] = 'X'
                    g_row += 1
                    # print([g_row, g_col])
            case '<':
                if g_col - 1 < 0:
                    patrol_layout[g_row][g_col] = 'X'
                    break
                elif g_col - 1 >= 0 and patrol_layout[g_row][g_col-1] == '.':
                    # inbounds of column moving right
                    # if g_row == 6 and g_col == 5:
                    #     print([g_row, g_col])
                    print([g_row, g_col])
                    patrol_layout[g_row][g_col] = 'X'
                    g_col -= 1
                    # print([g_row, g_col])
                elif g_col - 1 >= 0 and patrol_layout[g_row][g_col-1] == '#':
                    guard_orientation = '^'
                    orientation_change = True
                    patrol_layout[g_row][g_col] = 'X'
                    g_row -= 1
                    # print([g_row, g_col])
                elif g_col + 1 < len(patrol_layout[0]) and patrol_layout[g_row][g_col-1] == 'X':
                    patrol_layout[g_row][g_col] = 'X'
                    g_col -= 1
                    # print([g_row, g_col])
    
    for l in patrol_layout:
        print(''.join(l))

    x_count = 0
    for l in patrol_layout:
        x_count += ''.join(l).count('X')

    print(x_count)
                



    




if __name__ == '__main__':
    main()