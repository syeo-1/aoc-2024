
def split_file_line_contents_whitespace(file_contents, datatype='str'):
    '''
    given the lines of the file, split each line into individual elements that compose the line.
    Splits by whitespace in the line

    at the same time, detect the appropriate data type that should be used for each element of the line

    returns a list of lists, where each individual sublist contains a split line's contents composed of the
    appropriate datatype

    by default, leaves contents as strings. Pass in 'int' to convert contents of each split line to integers
    '''

    result = []

    for line in file_contents:
        if datatype == 'int':
            result.append([int(num) for num in line.split()])
        elif datatype == 'str':
            result.append(line.split())

    return result


def read_file_lines(filepath):
    '''
    read and split the contents of text input by newlines

    returns the contents of the file as a list of strings
    '''
    result = []
    with open(filepath) as file:
        for line in file:
            result.append(line.rstrip())

    return result

def transpose_matrix(m):
    '''
    takes a list of lists (ie. a matrix) and performs a transpose on it (rows become columns)
    and returns the transposed matrix as a new value
    '''
    return list(map(list, zip(*m)))

def main():
    file_lines = read_file_lines('input1.txt')
    processed_file_lines = split_file_line_contents_whitespace(file_lines, 'int')
    print(processed_file_lines)

if __name__ == '__main__':
    main()
    