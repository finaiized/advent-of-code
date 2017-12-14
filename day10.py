"""
Going through a backlog of Advent of Code right now, due to past exams
and binge-watching 13 Reasons Why.

Part One: 40 mins
I thought the logic for accessing wrap-around indexes would be hard,
because I initially wanted to access the sublist, reverse it, and write it back.
Instead, it is much easier to perform a swap between the beginning and end of the
sublist, and using modulo to handle any wrap-arounds.

Part Two: 30 mins
Holy reading Batman! This was a looong section with a lot of parts.
First mistake I made was thinking that '|' was the bitwise XOR operator in Python.
Also had to look up how to convert a character to its ASCII representation and
an integer to hex.
"""

SIZE = 256
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

def knot_hash(knot, lengths):
    current_position = 0
    skip_size = 0

    for l in lengths:
        # Reverse the order of the l elements in the list,
        # starting with the element at the current position
        reverse_sequence(knot, current_position, current_position + l - 1)

        # Move the current position forward by l plus the skip size
        current_position += (l + skip_size) % SIZE

        # Increase the skip size by one
        skip_size += 1


circular_list = list(range(SIZE))
part1_lengths = [int(l) for l in "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41".split(',')]

knot_hash(circular_list, part1_lengths)
print("The first two numbers multiplied give: {}".format(
    circular_list[0] * circular_list[1]
))

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

circular_list = list(range(SIZE))

print("The knot hash is {}".format(
    multiround_knot_hash(
        circular_list, 
        "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"
    )
))