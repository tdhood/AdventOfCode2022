with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day3/data.txt") as file:
    data = file.readlines()

def clean_data(input):
    result = [];
    for line in input:
        result.append(line.removesuffix('\n'))
    # print('cleaned', result)
    return result

clean_data = clean_data(data)

def get_chunks(lst, n):
   chunks = [lst[i:i + n] for i in range(0, len(lst), n)]
   return chunks

groups = get_chunks(clean_data, 3)
print('groups+++++++', groups)

def find_badge(group):
    # print('checking that Im getting what i think', group)
    

    word_1 = group[0]
    word_2 = group[1]
    word_3 = group[2]
    letters = []
    # print('word_1=', word_1, 'word_2=', word_2)
    for letter in word_1:
        if letter in word_2:
            letters.append(letter)

    # print('letters for group', letters)

    for letter in letters:
        if letter in word_3:
            return letter



def get_groups(groups):
    badges = [find_badge(group) for group in groups]
    return badges

badges = get_groups(groups)
print('badges for groups', badges)

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

get_sum_of_priorities(badges)