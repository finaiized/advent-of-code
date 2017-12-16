"""
Part One: 15 mins
Part Two: 1 min

This was kind of fun, even though it was simple. I realized that no matter if I used
a dict or list, I would incur a O(n) runtime to search for the program to exchange
in the exchange (x) or partner (p) moves. I guess I could have maintained two data
structures to do constant time lookups in both cases (name or index).

I'm pretty happy with my spin (s) instruction, using slices to make it super easy
to perform the shift. I also needed to use character - ord('a') to map letters
to [0, 25] ([a-z]).

Part two is literally just running it 1 billion times. That took a while.
I guess what's weird is that it actually depends how fast your computer
and programming language runs (in addition to algorithm of course, but better
algorithms usually take a bit more work upfront) if you want to get a good
ranking. I guess one way to do this is to detect what changed in the
array after one iteration from the initial one, then apply that change
(instead of all the ones that made that change) 1 billion times.

EDIT: Just kidding! It takes a looooong time if you do it this way. Once again,
Norvig has the answer: he noted that the dance pattern repeats after a while,
so if you take the cycle size, take the modulo of that with 1 billion,
you get how many cycles you need to simulate instead.
"""

programs = list(range(16))
moves = open("./data/day16.txt").read().split(',')

seen = set()

# 60 is the number of iterations until we see the initial configuration again.
# (Based on trying it).
# That means the cycle repeats. So instead of looping 1 billion times,
# loop 1000000000%60 = 40 times, and it's the same!
for _ in range(40):
    for move in moves:
        if move.startswith('s'):
            spin = int(move[1:])
            programs = programs[-spin:] + programs[0:-spin]
        elif move.startswith('x'):
            split = move[1:].split('/')
            exchangeA_index = int(split[0])
            exchangeB_index = int(split[1])
            temp = programs[exchangeA_index]
            programs[exchangeA_index] = programs[exchangeB_index]
            programs[exchangeB_index] = temp
        elif move.startswith('p'):
            split = move[1:].split('/')
            partnerA_name = split[0]
            partnerB_name = split[1]
            partnerA_value = ord(partnerA_name) - ord('a')
            partnerB_value = ord(partnerB_name) - ord('a')
            partnerA_index = programs.index(partnerA_value)
            partnerB_index = programs.index(partnerB_value)
            temp = programs[partnerA_index]
            programs[partnerA_index] = programs[partnerB_index]
            programs[partnerB_index] = temp

for i in programs:
    program_name = chr(ord('a') + i)
    print(program_name, end='')

print()