from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
)

def problem_dampener_report_is_safe(report):
    '''
    figure out which level to remove in a report in order to make it safe
    using functionality outline for problem dampener
    eg. if the report contains the given levels:
    1 3 2 4 5

    3 causes the report to be unsafe because 3->2 is decreasing when the sequence should be increasing

    by removing 3, the report becomes
    1 2 4 5

    which follow the constraints outlined in part 1
    '''

    '''
    good enough to just brute force it

   do so by just omitting one element at a time by using slicing operations
    '''
    for i in range(len(report)):
        modified_report = report[:i] + report[i:]

        # then check if the modified report is safe!

    # go through the report

    for i in range(1, len(report)):
        diff = report[i] - report[i-1]

    

def report_is_safe(report, status='same'):
    '''
    takes a report and based on its status of increasing or decreasing, checks if it is safe
    '''
    # print(report)
    if status == 'inc':
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            # print(diff)
            if diff == 0:
                return False
            elif diff <= 0 or diff >= 4:
                return False
    elif status == 'dec':
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff == 0:
                return False
            elif diff >= 0 or diff <= -4:
                return False
    elif status == 'same':
        pass

    return True

def main():
    file_lines = read_file_lines('input2.txt')
    reports = split_file_line_contents_whitespace(file_lines, 'int')

    # ##### PART 1 START #####
    # safe_count = 0
    # for report in reports:
    #     # find out whether the report should be increasing or decreasing
    #     first_two_level_difference = report[0] - report[1]
    #     if first_two_level_difference == 0:
    #         # unsafe
    #         continue
    #     elif first_two_level_difference > 0:
    #         # decreasing
    #         if report_is_safe(report, 'dec'):
    #             safe_count += 1
    #     elif first_two_level_difference < 0:
    #         # increasing
    #         if report_is_safe(report, 'inc'):
    #             safe_count += 1
    # print(safe_count)
    # ##### PART 1 END. done!!! #####

    ##### PART 2 START #####
    safe_count = 0
    for report in reports:
        # find out whether the report should be increasing or decreasing
        first_two_level_difference = report[0] - report[1]
        report_safe = False
        if first_two_level_difference > 0:
            # decreasing
            report_safe = report_is_safe(report, 'dec')
        elif first_two_level_difference < 0:
            # increasing
            report_safe = report_is_safe(report, 'inc')
        
        if not report_safe:
            modded_report_safe = False
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                first_two_level_difference_modified = modified_report[0] - modified_report[1]
                if first_two_level_difference_modified > 0:
                    # decreasing
                    modded_report_safe = report_is_safe(modified_report, 'dec')
                elif first_two_level_difference_modified < 0:
                    # increasing
                    modded_report_safe = report_is_safe(modified_report, 'inc')
                
                if modded_report_safe:
                    # print(modified_report)
                    safe_count += 1
                    break
                
        else:
            # print(report)
            safe_count += 1

    print(safe_count)
    ##### PART 2 END, DONE!!! #####



if __name__ == '__main__':
    main()
