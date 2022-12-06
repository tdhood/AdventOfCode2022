with open(
    r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day6/data.txt"
) as file:
    data = file.readlines()


def find_buffer(array_of_code):
    string = array_of_code[0]
    p1 = 0
    p2 = 1
    p3 = 2
    p4 = 3
    p5 = 4
    p6 = 5
    p7 = 6
    p8 = 7
    p9 = 8
    p10 = 9
    p11 = 10
    p12 = 11
    p13 = 12
    p14 = 13
    message_start = 14

    code_check = []
    length = len(string)

    while p14 <= len(string):
        code_check.append(string[p1])
        code_check.append(string[p2])
        code_check.append(string[p3])
        code_check.append(string[p4])
        code_check.append(string[p5])
        code_check.append(string[p6])
        code_check.append(string[p7])
        code_check.append(string[p8])
        code_check.append(string[p9])
        code_check.append(string[p10])
        code_check.append(string[p11])
        code_check.append(string[p12])
        code_check.append(string[p13])
        code_check.append(string[p14])
        if check_for_no_duplicates(code_check):
            print('message start', message_start)
            return message_start
        else:
            code_check = []
            p1 += 1
            p2 += 1
            p3 += 1
            p4 += 1
            p5 += 1
            p6 += 1
            p7 += 1
            p8 += 1
            p9 += 1
            p10 += 1
            p11 += 1
            p12 += 1
            p13 += 1
            p14 += 1
            message_start += 1
        

def check_for_no_duplicates(array):

    new_set = set(array)
    if(len(new_set) == len(array)):
        return True
    else:
        return False


find_buffer(data)