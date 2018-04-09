# Cube coordinates
# https://www.redblobgames.com/grids/hexagons/#coordinates
directions = {
    'nw': (-1, 1, 0),
    'ne': (1, 0, -1),
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'se': (1, -1, 0)
}

position = (0, 0, 0)
input_str = open("./data/day11.txt").read().split(',')
max_distance = 0
final_distance = 0

for ins in input_str:
    (x, y, z) = position
    (deltaX, deltaY, deltaZ) = directions[ins]
    position = (x + deltaX, y + deltaY, z + deltaZ)

    final_distance = (abs(position[0]) + abs(position[1]) + abs(position[2])) / 2
    if final_distance > max_distance:
        max_distance = final_distance

# Cube coordinates distance
print(f"The child process is {final_distance} steps away at the end")
print(f"The child process was at most {max_distance} steps away")