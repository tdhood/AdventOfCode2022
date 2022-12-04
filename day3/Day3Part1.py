with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day3/data.txt") as file:
    data = file.readlines()

# print('data=', data)
'''
a - z -> 1 - 26

A - Z -> 27 - 52
'''
def clean_data(input):
    result = [];
    for line in input:
        result.append(line.removesuffix('\n'))
    print('cleaned', result)
    return result

clean_data = clean_data(data)

def get_front_and_back_of_rucksack(rucksack):
    size = len(rucksack)
    size_of_each_compartment = round(size/2)
    front = rucksack[0:size_of_each_compartment]
    back = rucksack[size_of_each_compartment:]

    front_and_back = [front, back]

    return [front, back]

def separate_rucksacks(rucksacks):
    sorted_sacks = [get_front_and_back_of_rucksack(sack) for sack in rucksacks]
    print('sorted sacks+++++++++++++++++++++++', sorted_sacks)
    return sorted_sacks

sorted_rucksacks = separate_rucksacks(clean_data)

def find_priority_item(front_and_back):
    front = front_and_back[0]
    back = front_and_back[1]
    
    for item in front:
        if item in back:
            return item

rucksack_items = [find_priority_item(sack) for sack in sorted_rucksacks]
print('rucksack items', rucksack_items)

def get_value(char):

    if ord(char) >= 97 :
        value = ord(char) - 96
        print('item', char, 'value=', value)
        return value
    
    if ord(char) >= 65 and ord(char) <= 90:
        value = ord(char) - 64 + 26
        print('item', char, 'value=', value)
        return value

def get_sum_of_priorities(items):
    total = 0

    for item in items:
        total += get_value(item)
    
    print('total', total)
    return total

get_sum_of_priorities(rucksack_items)    

