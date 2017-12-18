from math import ceil, floor, sqrt
import itertools

input_num = 312051

def spiral_num(n):
    """
    Spiral 1 = 1 el
    Spiral 2 = 9 el (3x3)
    Spiral 3 = 25 el (5x5)

    So to get the size of the grid for each spiral, that's 2s - 1, where s is the spiral number.
    E.g. 2(3) - 1 = 5, for 5x5 grid

    Since each spiral has grid size x grid size elements, we can get the spiral number by taking the
    square root of the target number, and set it equal to the grid number:

    2s - 1 = sqrt(target num)

    Turns out we need to ceil to get the right number.
    """
    return ceil((sqrt(n) + 1) / 2)

# Part 1
spiral = spiral_num(input_num)
side_length = 2 * spiral - 1
num_elements_in_inner_spiral = (side_length - 2) ** 2
starting_num = num_elements_in_inner_spiral
distance = spiral - 1 + (side_length // 2)
ascending = False

while starting_num < input_num:
    starting_num += 1

    if ascending:
        distance += 1
    else:
        distance -= 1

    if distance == (side_length // 2):
        ascending = True
    elif distance == side_length - 1:
        ascending = False

print(distance)

# Part 2
def generate_spiral():
    x = 0
    y = 0
    s = 1

    yield (x, y)

    while True:
        # N right, N up, N + 1 left, N + 1 down

        for i in range(s):
            x += 1
            yield (x, y)

        for i in range(s):
            y -= 1
            yield (x, y)

        for i in range(s + 1):
            x -= 1
            yield (x, y)

        for i in range(s + 1):
            y += 1
            yield (x, y)

        s += 2

a = generate_spiral()
values = {(0, 0): 1}
next(a) # This is (0, 0) which we want to ignore since it has hardcoded value 1

for i in range(1, input_num):
    (x, y) = next(a)
    sum_of_neighbours = 0

    for (delta_x, delta_y) in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
        neighbour = (x + delta_x, y + delta_y)

        if neighbour in values:
            sum_of_neighbours += values[neighbour]

    values[(x, y)] = sum_of_neighbours

    if sum_of_neighbours > input_num:
        print(f"The first value that is larger than input is {sum_of_neighbours}")
        break
