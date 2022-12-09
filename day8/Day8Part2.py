with open(
    r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day8/data.txt"
) as file:
    data = file.readlines()

# print('data+++', data)


def clean_data(input):
    result = []
    for line in input:
        result.append(line.removesuffix('\n'))
    # print('cleaned', result)
    return result


clean_data = clean_data(data)
# print('clean data', clean_data)


def make_forest(input):

    forest = [line for line in input]
    return forest


forest = make_forest(clean_data)
print('forest=', forest)


def check_visibility_score(forest):
    
    top_edge = 1
    right_edge = len(forest[0]) - 2
    bottom_edge = len(forest) - 2
    left_edge = 1
    # visible_trees = 0 + (2 * len(forest[0]) + 2 * len(forest) - 4) 
    visibility_scores = []

    row_index = 1
    col_index = 1
    while row_index <= bottom_edge:
        while col_index <= right_edge:
            visibility_scores.append(get_visibility_score(row_index=row_index, col_index=col_index, forest=forest))
            col_index += 1
        row_index += 1
        col_index = 1

    max_score = max(visibility_scores)
    print('vis_score_array', visibility_scores)
    print('max_score', max_score)
    return max_score

def get_visibility_score(row_index, col_index, forest):
    top_edge = 0
    right_edge = len(forest[0]) - 1
    bottom_edge = len(forest) - 1
    left_edge = 0
    tree_height = forest[row_index][col_index]
    scores = []
    vis_score = 1

    scores.append(check_top_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, top_edge=top_edge, forest=forest))

    scores.append(check_bottom_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, bottom_edge=bottom_edge, forest=forest))
    
    scores.append(check_left_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, left_edge=left_edge, forest=forest))
    
    scores.append(check_right_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, right_edge=right_edge, forest=forest))
    
    for score in scores:
        vis_score *= score
      
    return vis_score

def check_top_trees(tree_height, row_index, col_index, top_edge, forest):
    count = 0
    if row_index == top_edge:
        return count

    while row_index -1 >= top_edge:
        height_being_checked = forest[row_index-1][col_index]
        if tree_height <= height_being_checked:
            count += 1
            return count
        else:
            count += 1
            row_index -= 1

    return count


def check_bottom_trees(tree_height, row_index, col_index, bottom_edge, forest):
    count = 0
    if row_index == bottom_edge:
        return count

    while row_index+1 <= bottom_edge:
        height_being_checked = forest[row_index+1][col_index]
        if tree_height <= height_being_checked:
            count += 1
            return count
        else:
            count += 1
            row_index += 1
            
    return count


def check_right_trees(tree_height, row_index, col_index, right_edge, forest):
    count = 0
    if col_index == right_edge:
        return count

    while col_index+1 <= right_edge:
        height_being_checked = forest[row_index][col_index+1]
        if tree_height <= height_being_checked:
            count += 1
            return count
        else:
            count +=1
            col_index += 1

    return count


def check_left_trees(tree_height, row_index, col_index, left_edge, forest):
    count = 0
    if col_index == left_edge:
        return count

    while col_index-1 >= left_edge:
        height_being_checked = forest[row_index][col_index-1]
        if tree_height <= height_being_checked:
            count += 1
            return count
        else:
            count += 1
            col_index -= 1

    return count

visibility_score = check_visibility_score(forest)