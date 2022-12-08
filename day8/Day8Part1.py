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


def check_trees(forest):
    
    top_edge = 1
    right_edge = len(forest[0]) - 2
    bottom_edge = len(forest) - 2
    left_edge = 1
    visible_trees = 0 + (2 * len(forest[0]) + 2 * len(forest) - 4) 

    row_index = 1
    col_index = 1
    while row_index <= bottom_edge:
        while col_index <= right_edge:
            if is_visible(row_index=row_index, col_index=col_index, forest=forest):
                visible_trees += 1
                col_index += 1
            else:
                col_index += 1
        row_index += 1
        col_index = 1

    print('visible_trees', visible_trees)
    return visible_trees


def is_visible(row_index, col_index, forest):
    top_edge = 0
    right_edge = len(forest[0]) - 1
    bottom_edge = len(forest) - 1
    left_edge = 0
    tree_height = forest[row_index][col_index]

    if check_top_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, top_edge=top_edge, forest=forest) or check_bottom_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, bottom_edge=bottom_edge, forest=forest) or check_left_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, left_edge=left_edge, forest=forest) or check_right_trees(tree_height=tree_height, row_index=row_index, col_index=col_index, right_edge=right_edge, forest=forest):
        return True
    else:
        return False


def check_top_trees(tree_height, row_index, col_index, top_edge, forest):
    while row_index -1 >= top_edge:
        height_being_checked = forest[row_index-1][col_index]
        if tree_height <= height_being_checked:
            return False
        else:
            row_index -= 1

    return True


def check_bottom_trees(tree_height, row_index, col_index, bottom_edge, forest):
    while row_index+1 <= bottom_edge:
        height_being_checked = forest[row_index+1][col_index]
        if tree_height <= height_being_checked:
            return False
        else:
            row_index += 1

    return True


def check_right_trees(tree_height, row_index, col_index, right_edge, forest):
    while col_index+1 <= right_edge:
        height_being_checked = forest[row_index][col_index+1]
        if tree_height <= height_being_checked:
            return False
        else:
            col_index += 1

    return True


def check_left_trees(tree_height, row_index, col_index, left_edge, forest):
    while col_index-1 >= left_edge:
        height_being_checked = forest[row_index][col_index-1]
        if tree_height <= height_being_checked:
            return False
        else:
            col_index -= 1

    return True

visibility = check_trees(forest)

