import re
with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day5/data.txt") as file:
    data = file.readlines()



def clean_data(input):
    result = [];
    for line in input:
        result.append(line.removesuffix('\n'))
    # print('cleaned', result)
    return result

clean_data = clean_data(data)
# print('data', clean_data)

crates = {
    1: ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
    2: ['H', 'F', 'R'],
    3: ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
    4: ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
    5: ['P', 'S', 'M', 'J', 'H'],
    6: ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
    7: ['P', 'T', 'H', 'N', 'M', 'L'], 
    8: ['F', 'D', 'Q', 'R'],
    9: ['D', 'S', 'C', 'N', 'L', 'P', 'H']
}

instructions = clean_data[10:]
print('instructions', instructions)

def move_crate(move_from, move_to, n, dict):
    count = 0
    crates_to_move = []

    while count < n:
        crates_to_move.append(dict[move_from].pop())
        count += 1
    
    while len(crates_to_move) > 0:
        crate = crates_to_move.pop()
        dict[move_to].append(crate)

    return dict

def parse_instructions(string):
    values = re.findall(r'\d+', string)
    n = int(values[0])
    move_from = int(values[1])
    move_to = int(values[2])
    # print('values', values)
    return [move_from, move_to, n]
    


def run_instructions(instructions, dict):
    for instruction in instructions:
        (move_from, move_to, n) = parse_instructions(instruction)
        move_crate(move_from, move_to, n, dict)
    print('crates', dict)
    return dict

run_instructions(instructions, crates)