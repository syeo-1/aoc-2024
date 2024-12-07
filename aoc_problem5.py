from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix
)

from collections import defaultdict

def correct_given_update(update, rule_map, rule_list):
    # find out which rules have been violated
    invalid_rules = []
    for i in range(len(update)-1, -1, -1):
        instructions_to_check = update[:i]
        for instruction in instructions_to_check:
            if instruction in rule_map[update[i]]:
                invalid_rules.append([update[i], instruction])
    # print(invalid_rules)
    # print(update)

    for invalid_rule in invalid_rules:
        # perform the swaps
        first = update.index(invalid_rule[0])
        second = update.index(invalid_rule[1])
        
        if first > second:
            update[first], update[second] = update[second], update[first]

    # do another run through of rule_list to ensure nothing's missed
    # since during swapping some other error may have been introduced
    for rule in rule_list:
        if rule[0] in update and rule[1] in update and rule not in invalid_rules:
            # check if index of first element in the update is less than
            # index of the second element in the update
            first = update.index(rule[0])
            second = update.index(rule[1])
            if first > second:
                update[first], update[second] = update[second], update[first]


            # if it isn't, then perform a swap
    # print(update)
    return int(update[len(update)//2])

def main():
    # rules = read_file_lines('input_5_1.txt')
    # orders = read_file_lines('input_5_2.txt')
    rules = read_file_lines('input5_sample1.txt')
    orders = read_file_lines('input5_sample2.txt')

    rule_list = [rule.split('|') for rule in rules]
    processed_updates = [order.split(',') for order in orders]
    # print(rule_list)

    rule_map = defaultdict(list)
    for rule in rule_list:
        rule_map[rule[0]].append(rule[1])
    
    # print(rule_map)

    # so what i need to do is, using the default dict map
    # just iterate in reverse for each update list
    # if any numbers before the current number in the update list
    # are in the rule list, then a violation has occured
    # and the update instruction is invalid
    valid_updates = []
    invalid_updates = []
    for update in processed_updates:
        update_is_valid = True
        for i in range(len(update)-1, -1, -1):
            instructions_to_check = update[:i]
            for instruction in instructions_to_check:
                if instruction in rule_map[update[i]]:
                    update_is_valid = False
                    break
            if not update_is_valid:
                break
        
        if update_is_valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    # print(valid_updates)

    result_sum = 0
    for valid_update in valid_updates:
        result_sum += int(valid_update[len(valid_update)//2])

    # part 2
    # print(invalid_updates)
    corrected_update_sum = 0
    for invalid_update in invalid_updates:
        corrected_update_sum += correct_given_update(invalid_update, rule_map, rule_list)
    
    print(corrected_update_sum)
        

    # print(order)

if __name__ == '__main__':
    main()