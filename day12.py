"""
A little rusty today, maybe because I didn't do the last two because of exams?

# Part One
Solved in 09:25, Rank 234. Made a lot of small mistakes resulting
in a lot of run time errors I had to go back and fix one at a time.
Overall algorithm came pretty quickly though.

# Part Two
Solved at 14:47, Rank 257 (~5 mins after part one). Algorithm
came to be immediately, but I actually didn't know how to get
any element from a set without removing it (I actually didn't need to;
I got rid of it). It's next(iter(set)). I was also off-by-one
the first time I submitted my solution, which I immediately realized.

Anyhow, I revamped this solution quite a bit. The overall structure
is the same, but renamed things and moved things into functions.
"""
input_str = open("./data/day12.txt").read().split('\n')

connected_to = {}
for line in input_str:
    line = line.split(" <-> ")
    program_id = int(line[0])

    if program_id not in connected_to:
        connected_to[program_id] = set()

    pipes = [connected_program.strip() for connected_program in line[1].split(',')]

    for pipe in pipes:
        connected_to[program_id].add(int(pipe))

def programs_in_group_with(program_id, connections):
    """Returns the number of programs in a group with the given program.

    Algorithm: Start at the given program, and follow it's connections
    until we've visited them all. All reachable programs are in the same group.
    """
    to_visit = [program_id]
    visited = set()

    while True:
        if not to_visit:
            return len(visited)

        next_program = to_visit.pop()
        if next_program in visited:
            continue

        visited.add(next_program)
        
        connected_to = connections[next_program]
        for p in connected_to:
            to_visit.append(p)

print("{} programs are in a group with program ID 0".format(
    programs_in_group_with(0, connected_to))
)

def total_groups(connections):
    """Returns the number of disjoint groups of programs.

    Algorithm: Find the group of an arbitrary program.
    Then, find all programs not in that group, and repeat until
    all programs are in a group.
    """

    groups = 0
    all_programs = set(connections.keys())
    visited = set()
    not_visited = all_programs

    while not_visited:
        to_visit = [not_visited.pop()]
        groups += 1

        while to_visit:
            next_program = to_visit.pop()
            if next_program in visited:
                continue

            visited.add(next_program)
            connected_to = connections[next_program]

            for p in connected_to:
                to_visit.append(p)
        
        not_visited = all_programs - visited

    return groups

print("There are {} groups in total".format(total_groups(connected_to)))