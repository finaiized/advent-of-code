input_str = open("./data/day19.txt").read().split('\n')
input_str = [[c for c in line] for line in input_str]

# Find first | in first row as the starting position
loc_x = 0
loc_y = input_str[0].index('|')

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

orthogonal_directions = {
    "down": ["left", "right"],
    "up": ["left", "right"],
    "left": ["up", "down"],
    "right": ["up", "down"],
}

letters = []
steps = 0
direction = "down"
grid_size_x = len(input_str)
grid_size_y = len(input_str[0])

def character_exists(x, y):
    if (0 <= x and x < grid_size_x - 1 and
        0 <= y and y < grid_size_y - 1 and
        input_str[x][y] != ' '):
        return True

    return False

while True:
    c = input_str[loc_x][loc_y]
    print(c, direction)

    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters.append(c)

    if c == ' ':
        break

    steps += 1

    (offset_x, offset_y) = directions[direction]
    next_x = loc_x + offset_x
    next_y = loc_y + offset_y

    if character_exists(next_x, next_y):
        # Can continue in this direction
        loc_x = next_x
        loc_y = next_y
    else:
        found_new_direction = False

        # Try orthogonal directions
        for orth_direction in orthogonal_directions[direction]:
            (offset_x, offset_y) = directions[orth_direction]
            next_x = loc_x + offset_x
            next_y = loc_y + offset_y

            if character_exists(next_x, next_y):
                direction = orth_direction
                loc_x = next_x
                loc_y = next_y
                found_new_direction = True
                break
        
        if not found_new_direction:
            # No more path to follow in any direction
            break
    
print(steps, ''.join(letters))