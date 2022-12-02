with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day1/data.txt") as file:
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

def total(list):
    total = 0
    for x in list:
        total += x
    return total

def find_calories_per_elf(elf_packs):
    elves = [total(calories) for calories in elf_packs]
    return elves

calories_per_pack = find_calories_per_elf(elf_packs)
print('total calories per fact+++++++', calories_per_pack)

def find_max_3_elves(calories):
    sorted_calories = sorted(calories, reverse=True)
    top_3_calories = sorted_calories[0:3]

    total = 0
    for cal in top_3_calories:
        total += cal
    return total
    print('sorted=====', sorted_calories)
    print('top 3', top_3_calories)
    print('total for top 3', total)
print('find elf with the most' ,find_max_3_elves(calories_per_pack))