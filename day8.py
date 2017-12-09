"""
# Part 1
Solved with rank 126! In 7 mins, 48 seconds

Clearly, this was my best day yet! I didn't have any real problems in this question,
just needed to code it.

I saw that the question was an instruction-stream type of question, which is generally easy
(though if it had bit shifting it might take a bit of work).

Once again, I expected that parsing would be the most difficult part.
It didn't turn out to be because I did it as stupidly as possible,
which is to say to parse the string with delimiters like " -> " to get
exactly what I need without any extra spaces, or needing to piece together
a string if I had split just by spaces.

I felt like my code was pretty clean despite doing it fast. I could have shaved
off a good amount of time by just using one character variable names,
though if I had to debug, it would be a pain figuring things out.
The only thing I added to this solution was to read from a file instead
of a string, comments, and clearer print messages.

# Part 2
Solved with rank 107! 45 seconds after part 1 was solved

The second part was a really easy change, as it was just tracking the
max register value ever. This was just an extra condition to check
after every register was updated.

Overall, an easy and fun day. Didn't have much to do this night
since I just had a midterm that afternoon and I wanted to take a break
(by coding of course!).
"""

input_str = open("data/day8.txt").read()
lines = input_str.split('\n')
registers = dict()
max_register_value_ever = 0 # Used for Part 2

for line in lines:
    tokens = line.split(' ')
    register = tokens[0]

    if register not in registers:
        registers[register] = 0

    command = tokens[1]
    amount = int(tokens[2])

    # E.g. for instruction "b inc 5 if a > 1":
    # - register is "b"
    # - command is "inc"
    # - amount is 5

    if_statement = line.split(' if ')
    if_statement = if_statement[1]
    if_components = if_statement.split(' ')

    if_register = if_components[0]
    if_command = if_components[1]
    if_num = int(if_components[2])

    # E.g. for instruction "b inc 5 if a > 1":
    # - if_register is "a"
    # - if_command is ">"
    # - if_num is 1

    # Default value for a register is 0
    reg_value = registers[if_register] if if_register in registers else 0

    command_passes = False
    if if_command == ">":
        command_passes = reg_value > if_num
    elif if_command == "<":
        command_passes = reg_value < if_num
    elif if_command == "<=":
        command_passes = reg_value <= if_num
    elif if_command == ">=":
        command_passes = reg_value >= if_num
    elif if_command == "!=":
        command_passes = reg_value != if_num
    elif if_command == "==":
        command_passes = reg_value == if_num
    else:
        print("Unknown operator in if: {}".format(if_command))

    if command_passes:
        if command == 'inc':
            registers[register] += amount
        elif command == 'dec':
            registers[register] -= amount
        else:
            print("Unknown command: {}".format(command))

    # Part 2: Keep track of max register value over all time
    if registers[register] > max_register_value_ever:
        max_register_value_ever = registers[register]

print("Max final register value", max(registers.values()))
print("Max register value ever: {}".format(max_register_value_ever))
