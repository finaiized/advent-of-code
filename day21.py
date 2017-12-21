from math import sqrt

input_str = """.#.
..#
###""".split('\n')

matrix = [[True if c == '#' else False for c in row] for row in input_str]

def concise_pattern_to_matrix(pattern):
    pattern = pattern.split('/')

    matrix = []
    for p in pattern:
        temp = []
        for c in p:
            if c == '#':
                temp.append(True)
            else:
                temp.append(False)

        matrix.append(temp)

    return matrix

with open("./data/day21.txt") as data:
    rules_str = data.read()

rules = (s.split(" => ") for s in rules_str.split('\n'))
rules = {split[0]: concise_pattern_to_matrix(split[1]) for split in rules}

def rotate(matrix):
    size = len(matrix)
    layer_count = size // 2

    for layer in range(0, layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last-offset]
            left_side = matrix[last-offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom

    return matrix

def horizontal_flip(matrix):
    size = len(matrix)
    layer_count = size // 2
    
    for layer in range(layer_count):
        temp = matrix[layer]
        matrix[layer] = matrix[size - layer - 1]
        matrix[size - layer - 1] = temp

    return matrix
        
def vertical_flip(matrix):
    size = len(matrix)
    layer_count = size // 2

    for layer in range(layer_count):
        for i in range(size):
            temp = matrix[i][layer]
            matrix[i][layer] = matrix[i][size - layer - 1]
            matrix[i][size - layer - 1] = temp

    return matrix            

def matrix_to_concise_pattern(matrix):
    pattern = ""

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                pattern += "#"
            else:
                pattern += "."

        pattern += "/"

    return pattern[:-1] # Remove final '/'

def match_rule(matrix):
    pattern = matrix_to_concise_pattern(vertical_flip(matrix))
    if pattern in rules:
        return rules[pattern]
    vertical_flip(matrix) # Undo

    pattern = matrix_to_concise_pattern(horizontal_flip(matrix))
    if pattern in rules:
        return rules[pattern]

    horizontal_flip(matrix) # Undo

    for _ in range(4):
        pattern = matrix_to_concise_pattern(rotate(matrix))
        if pattern in rules:
            return rules[pattern]

        pattern = matrix_to_concise_pattern(vertical_flip(matrix))
        if pattern in rules:
            return rules[pattern]
        vertical_flip(matrix)

        pattern = matrix_to_concise_pattern(horizontal_flip(matrix))
        if pattern in rules:
            return rules[pattern]
        horizontal_flip(matrix)        

    raise AssertionError("Can't find matching pattern!")

def merge_submatrices(matrices):
    matrix = []
    size = int(sqrt(len(matrices)))
    for i in range(size):
        # set of matrices = i * size + 0, i * size + 1, i * size + 2
        for j in range(len(matrices[0])):
            temp = []    
            for k in range(size):
                temp.extend(matrices[i * size + k][j])

            matrix.append(temp)

    return matrix

def split(matrix):
    # Split matrix into twos or threes
    divisor = 3
    if len(matrix) % 2 == 0:
        divisor = 2

    size = len(matrix) // divisor

    submatrices = []
    for j in range(0, len(matrix), divisor): # Down
        for i in range(0, len(matrix), divisor): # Across
            small_matrix = []
            for k in range(divisor):
                small_matrix.append(matrix[j + k][i:i+divisor])

            submatrices.append(small_matrix)
    
    return submatrices

for i in range(18):
    split_matrix = split(matrix)
    submatrices = []
    for m in split_matrix:
        new_matrix = match_rule(m)
        submatrices.append(new_matrix)
    matrix = merge_submatrices(submatrices)

    if i == 4:
        print(f"After 5 iterations, {sum(r.count(True) for r in matrix)} pixels are on")

    if i == 17:
        print(f"After 18 iterations, {sum(r.count(True) for r in matrix)} pixels are on")
