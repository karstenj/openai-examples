def solution_2022_3_1(input_list):
    result = 0

    for rucksack in input_list:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]

        for char in set(first_compartment):
            if char in second_compartment:
                if char.islower():
                    result += ord(char) - 96
                else:
                    result += ord(char) - 38
    return result