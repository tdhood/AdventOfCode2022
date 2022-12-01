with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day1/part1/data.txt") as file:
    data = file.readlines()

def clean_data(input):
    # print('input++++++++++++++', input)

    data = [line.removesuffix('\n') for line in input]
  
    return data
    
clean_data = clean_data(data)
# print("clean_data+++++", clean_data)

def make_elf_packs(data):

    pack = []
    elf_packs = []

    for line in data:
        if line != '':
            pack.append(int(line))
        if line == '':
            elf_packs.append(pack)
            pack = []
    return elf_packs

elf_packs = make_elf_packs(clean_data)
# print('elf packs++++', make_elf_packs(clean_data))

def total(array):
    total = 0
    for x in array:
        total += x
    return total

def find_calories_per_elf(elf_packs):
    elves = {i: total(calories) for i, calories in enumerate(elf_packs, 1)}
    return elves
    

elves_and_packs = find_calories_per_elf(elf_packs)
print('elves and total calories+++++++', elves_and_packs)

def find_max(dict):
    calories = list(dict.values())
    elves = list(dict.keys())
    max_calories = max(calories)
    print('max_cal=====', max_calories)
    elf_with_most_calories = elves[calories.index(max_calories)]
    print('elf_with_most_calories', elf_with_most_calories)
print('find elf with the most' ,find_max(elves_and_packs))

