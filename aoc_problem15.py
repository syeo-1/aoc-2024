from aoc_helper import *
from itertools import chain

def main():
    layout = read_file_lines('input15_1.txt')
    instructions = read_file_lines('input15_2.txt')

    
    d = [
        (-1, 0),
        (1, 0), 
        (0, -1),
        (0, 1)
    ]

    # can use d[ds.index('^')] to lookup the proper direction point/tuple 
    ds = "^v<>"

    # print(layout)
    # print(instructions)

    layout_processed = [list(s) for s in layout]

    # check the second highest voted answer on how to flatten a 2d nested list using chain function and splat operator: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    instructions_processed = list(chain(*[list(s) for s in instructions]))

    starting_point = None
    for i, r in enumerate(layout):
        for j, c in enumerate(r):
            if c == '@':
                # adding breaks appropriately would give negligible speed improvements, so no need
                starting_point = [i, j]

    # since i know the starting point already, just set it to be a dot now
    layout_processed[starting_point[0]][starting_point[1]] = '.'
                
    
    print(starting_point)

    x, y = starting_point[0], starting_point[1]
    # refer to this video, credits to Larry: https://www.youtube.com/watch?v=YSfktJ2RVqU
    for c in instructions_processed:
        # unpack direction tuple
        dx, dy = d[ds.index(c)]

        # get the new position that the @ should be at
        nx, ny = x + dx, y + dy

        if layout_processed[nx][ny] == '.':
            x, y = nx, ny
            continue

        if layout_processed[nx][ny] == '#':
            continue

        if layout_processed[nx][ny] == 'O':
            bx, by = x + dx, y+ dy

            while layout_processed[bx][by] == 'O':
                bx, by = bx + dx, by + dy

            if layout_processed[bx][by] == '#':
                continue

            assert(layout_processed[bx][by] == '.')
            layout_processed[bx][by] = 'O'
            layout_processed[nx][ny] = '.'
            x, y = nx, ny

    
    total = 0
    for x in range(len(layout_processed)):
        for y in range(len(layout_processed[0])):
            if layout_processed[x][y] == 'O':
                total += x * 100 + y
    print(total)




    


        

    # print(layout_processed)
    # print(instructions_processed)

if __name__ == '__main__':
    main()