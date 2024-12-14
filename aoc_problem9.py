from aoc_helper import *

def main():
    # initial_input = read_file_lines('input9_sample2.txt')
    initial_input = read_file_lines('input9.txt')
    diskmap = initial_input[0]
    # generate the diskmap char list
    diskmap_charlist = []
    isfile = True
    disk_id = 0
    for c in diskmap:
        if isfile:
            for _ in range(int(c)):
                diskmap_charlist.append(disk_id)
            disk_id += 1
            isfile = False
        else:
            for _ in range(int(c)):
                diskmap_charlist.append('.')
            isfile = True
    # print(''.join(str(c) for c in diskmap_charlist))

    dot = 0
    end = len(diskmap_charlist)-1

    while dot < end:
        if diskmap_charlist[dot] == '.' and diskmap_charlist[end] != '.':
            diskmap_charlist[dot], diskmap_charlist[end] = diskmap_charlist[end], diskmap_charlist[dot]
            dot += 1
            end -= 1
        
        if diskmap_charlist[dot] != '.':
            dot += 1
        if diskmap_charlist[end] == '.':
            end -= 1
            # continue

    # print(''.join(str(c) for c in diskmap_charlist))

    checksum_val = 0
    for i, c in enumerate(diskmap_charlist):
        if c == '.':
            break
        else:
            checksum_val += i * int(c)
    # print(''.join(str(c) for c in diskmap_charlist))
    print(checksum_val)


if __name__ == '__main__':
    main()