"""
Part One: 15 mins
Part Two: 10 mins

"""

with open("./data/day20.txt") as data:
    input_str = data.read().split('\n')

# Part One
distances = []
for line in input_str:
    splits = line.split(', ')
    pos = [int(c) for c in splits[0][3:-1].split(',')]
    vel = [int(c) for c in splits[1][3:-1].split(',')]
    acc = [int(c) for c in splits[2][3:-1].split(',')]

    distance = 0
    for _ in range(500):
        for i in range(3):
            vel[i] += acc[i]
            pos[i] += vel[i]

        distance += abs(pos[0]) + abs(pos[1]) + abs(pos[2])

    distances.append(distance)

print(distances.index(min(distances)))

# Part Two
remaining = [True] * len(input_str)
pos = []
vel = []
acc = []

for (i, line) in enumerate(input_str):
    splits = line.split(', ')
    pos.append([int(c) for c in splits[0][3:-1].split(',')])
    vel.append([int(c) for c in splits[1][3:-1].split(',')])
    acc.append([int(c) for c in splits[2][3:-1].split(',')])

for tick in range(100):
    for i in range(len(pos)):
        if remaining[i]:
            for k in range(3):
                vel[i][k] += acc[i][k]
                pos[i][k] += vel[i][k]

    for j in range(len(input_str)):
        if not remaining[j]: continue

        for k in range(j + 1, len(input_str)):
            if (pos[j][0] == pos[k][0] and
                pos[j][1] == pos[k][1] and
                pos[j][2] == pos[k][2]):
                remaining[j] = False
                remaining[k] = False

print(remaining.count(True))


        

    

    

    