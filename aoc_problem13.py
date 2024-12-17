from aoc_helper import *

from collections import namedtuple
import numpy as np

def main():
    input_text = read_file_lines('input13_sample.txt')
    input_text = [t for t in input_text if t != '']

    buttonA = namedtuple('buttonA', ['x', 'y'])
    buttonB = namedtuple('buttonB', ['x', 'y'])
    prize = namedtuple('Prize', ['x','y'])

    prize_info_all = []
    for i in range(0, len(input_text), 3):
        prize_dict = {}
        
        buttonA_info = input_text[i].split(': ')
        prize_dict['A'] = buttonA(x=int(buttonA_info[1].split(', ')[0].split('+')[1]), y=int(buttonA_info[1].split(', ')[1].split('+')[1]))
        
        buttonB_info = input_text[i+1].split(': ')
        prize_dict['B'] = buttonB(x=int(buttonB_info[1].split(', ')[0].split('+')[1]), y=int(buttonB_info[1].split(', ')[1].split('+')[1]))

        prize_info = input_text[i+2].split(': ')
        prize_dict['Prize'] = prize(x=int(prize_info[1].split(', ')[0].split('=')[1]), y=int(prize_info[1].split(', ')[1].split('=')[1]))
        # print(prize_dict['Prize'])

        prize_info_all.append(prize_dict)
        # print(prize_info_all)

    # print(prize_info_all)
        
    for info in prize_info_all:
        a = info['A']
        b = info['B']
        cur_prize = info['Prize']

        equation_matrix = np.array([[a.x, a.y], [b.x, b.y]])
        soln_matrix = np.array([[cur_prize.x], [cur_prize.y]])

        try:
            equation_solution = np.linalg.solve(equation_matrix, soln_matrix)
            round_solution = np.round(equation_solution)
            if np.allclose(np.dot(equation_matrix, round_solution) - soln_matrix, np.zeros(2)):
                print(equation_solution)
            else:
                print('no integer solution')
                print(round_solution)
        except:
            print('no solution')







        
    
    # print(input_text)



if __name__ == '__main__':
    main()