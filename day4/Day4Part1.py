import re

with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day4/data.txt") as file:
    data = file.readlines()

# print('data+++', data)

def clean_data(input):
    result = [];
    for line in input:
        result.append(line.removesuffix('\n'))
    # print('cleaned', result)
    return result

clean_data = clean_data(data)
print('clean data', clean_data)

def compare_sections(sections):
    count = 0
    for section in sections:
        section = section.split(',')
        print('sections++++++++', section)
        section_1 = section[0]
        section_2 = section[1]

        section_1_start = int(section_1.split('-')[0])
        section_1_end = int(section_1.split('-')[1])
        section_2_start = int(section_2.split('-')[0])
        section_2_end = int(section_2.split('-')[1])


        if section_1_start <= section_2_start and section_1_end >= section_2_end:
            count += 1
            print('counted')
    
        elif section_2_start <= section_1_start and section_2_end >= section_1_end:
            count +=  1
            print('counted')

    print('count=', count)
    return count



count = compare_sections(clean_data)

