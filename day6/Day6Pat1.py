with open(
    r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day6/data.txt"
) as file:
    data = file.readlines()


def find_buffer(array_of_code):
    string = array_of_code[0]
    pointer1 = 0
    pointer2 = 1
    pointer3 = 2
    pointer4 = 3
    pointer5 = 4

    length = len(string)

    while pointer4 <= len(string):
        if (
            string[pointer1] != string[pointer2]
            and string[pointer1] != string[pointer3]
            and string[pointer1] != string[pointer4]
            and string[pointer2] != string[pointer3]
            and string[pointer2] != string[pointer4]
            and string[pointer3] != string[pointer4]
        ):
            print('code', string[pointer1], string[pointer2], string[pointer3], string[pointer4])
            print("pointer5++++", pointer5)
            return string[pointer5]
        else:
            pointer1 += 1
            pointer2 += 1
            pointer3 += 1
            pointer4 += 1
            pointer5 += 1

find_buffer(data)