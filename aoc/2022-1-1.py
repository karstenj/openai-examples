def solution_2022_1_1(input_list):
    result = 0
    current_total = 0

    for item in input_list:
        if item == '':
            result = max(result, current_total)
            current_total = 0
        else:
            current_total += int(item)
    return result