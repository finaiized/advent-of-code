SIZE = 256

# Begin Day 10 code
def reverse_sequence(lst, i, j):
    """Reverse the sequence bounded by i and j in place.

    i and j do not have to be bounded by the length of the list:
    they will automatically wrap around lst, making lst
    a circular array."""

    if j < i:
        return
    
    lst_len = len(lst)
    subsequence_length = j - i + 1
    start_index = i % lst_len
    end_index = j % lst_len


    for k in range(subsequence_length // 2):
        swap_start_index = (start_index + k) % lst_len
        swap_end_index = (end_index - k) % lst_len

        temp = lst[swap_start_index]
        lst[swap_start_index] = lst[swap_end_index]
        lst[swap_end_index] = temp

def sparse_hash(dense_hash):
    hash = []

    for i in range(0, len(dense_hash), 16):
        xor = 0
        for j in range(0, 16):
            xor ^= dense_hash[i + j]

        hash.append(xor)

    return hash

def sparse_hash_to_hex(sparse_hash):
    return ''.join(["{:02x}".format(i) for i in sparse_hash])

def multiround_knot_hash(knot, length_str):
    lengths = [ord(l) for l in length_str]
    lengths += [17, 31, 73, 47, 23]

    current_position = 0
    skip_size = 0

    for _ in range(64):
        for l in lengths:
            # Reverse the order of the l elements in the list,
            # starting with the element at the current position
            reverse_sequence(knot, current_position, current_position + l - 1)

            # Move the current position forward by l plus the skip size
            current_position += (l + skip_size) % SIZE

            # Increase the skip size by one
            skip_size += 1

    hash = sparse_hash(knot)
    return sparse_hash_to_hex(hash)

# End Day 10 code

def hex_string_to_binary(hex):
    return ''.join(["{:04b}".format(int(c, 16)) for c in hex])

KEY = "hxtvlmkl"

# Part One
set_bits = 0
for i in range(0, 128):
    circular_list = list(range(SIZE))
    input_for_row = KEY + f"-{i}"
    hash = multiround_knot_hash(circular_list, input_for_row)
    set_bits += hex_string_to_binary(hash).count("1")

print(f"{set_bits} locations are used")

# Part Two
grid = []
for i in range(0, 128):
    circular_list = list(range(SIZE))
    input_for_row = KEY + f"-{i}"
    hash = multiround_knot_hash(circular_list, input_for_row)
    grid.append([int(c) for c in hex_string_to_binary(hash)])

groups = 0
visited = set()
for (i, row) in enumerate(grid):
    for (j, col) in enumerate(row):
        if grid[i][j] == 1 and (i, j) not in visited:
            groups += 1
            # Set bit that isn't part of any group yet
            # Flood fill from here
            to_visit = [(i, j)]
            local_visited = set()

            while to_visit:
                (r, c) = to_visit.pop()
                if grid[r][c] == 1:
                    visited.add((r, c))
                    local_visited.add((r, c))

                    left = (r, max(0, c - 1))
                    right = (r, min(127, c + 1))
                    up = (max(r - 1, 0), c)
                    down = (min(r + 1, 127), c)

                    if left not in local_visited:
                        local_visited.add(left)
                        to_visit.append(left)
                    if right not in local_visited:
                        local_visited.add(right)
                        to_visit.append(right)
                    if up not in local_visited:
                        local_visited.add(up)
                        to_visit.append(up)
                    if down not in local_visited:
                        local_visited.add(down)
                        to_visit.append(down)

print(f"There are {groups} groups of used squares")
            