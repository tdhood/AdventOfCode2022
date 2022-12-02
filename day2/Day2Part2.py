with open(r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day2/data.txt") as file:
    data = file.readlines()

''' points:

    Rock: 1 A
    Paper: 2 B
    Scissors: 3 C

    win: 6 Z
    draw: 3 Y
    lose: 0 X
'''

print('data=', data)

def clean_data(input):
    result = [];
    for line in input:
        result.append(line.removesuffix('\n'))
    print('cleaned', result)
    return result

clean_data = clean_data(data)

def rock_paper_scissors(string):
    score = 0
    if string[0] == 'A':
        #opp played Rock
        if string[2] == 'Y':
            # hero played Rock
            # draw
            score += 1
            score += 3
        if string[2] == 'Z':
            # hero played Paper
            # win
            score += 2
            score += 6
        if string[2] == 'X':
            # hero played Scissors
            # lose
            score += 3
            score += 0
    if string[0] == 'B':
        #opp played Paper
        if string[2] == 'X':
            # hero played Rock
            # lose
            score += 1
            score += 0
        if string[2] == 'Y':
            # hero played Paper
            # draw
            score += 2
            score += 3
        if string[2] == 'Z':
            # hero played Scissors
            # win
            score += 3
            score += 6
    if string[0] == 'C':
        #opp played Scissors
        if string[2] == 'Z':
            # hero played Rock
            # win
            score += 1
            score += 6
        if string[2] == 'X':
            # hero played Paper
            # lose
            score += 2
            score += 0
        if string[2] == 'Y':
            # hero played Scissors
            # draw
            score += 3
            score += 3
    
    return score

def get_score(game_results):
    score = 0
    for hand in game_results:
       score += rock_paper_scissors(hand)
    print('max score', score)
    return score

get_score(clean_data)
