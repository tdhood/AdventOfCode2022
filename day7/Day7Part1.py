with open(
    r"/home/kestrel/Documents/CodingProjects/AdventOfCode2022/day7/data.txt"
) as file:
    data = file.readlines()

# print('data+++', data)

def clean_data(input):
    result = [];
    for line in input:
        result.append(line.removesuffix('\n'))
    # print('cleaned', result)
    return result

clean_data = clean_data(data)
# print('clean data', clean_data)

''' 
cd / or dir name = create a node
ls -everything before $ is child - creates branches from node
'''



class TreeNode(object):
    def __init__(self, name=None, val=0, children={}, parent=None):
        self.name = name
        self.val = val
        self.children = {}
        self.parent = parent

def build_tree(input_data):
    dir_size = 0
    root = handle_cd(input_data[0], parent=None)
    parent = root
    for line in input_data[1:]:
        if '$' in line:
            if 'cd' in line and '..' not in line:
                new_node = handle_cd(line, parent=parent)
                parent.children[new_node.name] = new_node
                parent = new_node
            if 'dir' in line:
                new_child = handle_dir(line)
                parent.children[new_child] = None
            if 'cd' in line and '..' in line:
                parent = parent.parent
        if line[0].isnumeric():
            new_node = handle_file(line, parent=parent)
            parent.children[new_node.name] = new_node
    return root


def handle_cd(string, parent):
    split_array = string.split(' ')
    new_node = TreeNode(name=split_array[2], parent=parent)
    return new_node

def handle_dir(string):
    split_array = string.split(' ')
    new_child = split_array[1]
    return new_child

def handle_file(string, parent):
    split_array = string.split(' ')
    new_node = TreeNode(name=split_array[1], val=int(split_array[0]), parent=parent)
    return new_node

root = build_tree(clean_data)

def get_deletable_directories(root_node):
    total = 0
    dirs = {}

    for child in root_node.children:
        if child.val == 0:
            get_deletable_directories(child)
        else: 



# part one 1348005
# part two 12785886