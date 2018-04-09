# Part 1
# Messed up on line reading again, forgot about the empty line case!
# Also misread the instructions, thought any visited instruction gets incremented,
# which complicated the solution a bit (and made it wrong)
# 15 mins

with open("./data/day5.txt") as data:
    instructions = [int(n) for n in data.read().split('\n') if n != '']
    instructions_length = len(instructions)
    instruction_index = 0
    steps = 0

    while instruction_index >= 0 and instruction_index < instructions_length:
        steps += 1
        jump = instructions[instruction_index]
        instructions[instruction_index] += 1
        instruction_index += jump

    print("Took {} steps to exit".format(steps))

# Part 2
# 2 mins
# Trivial change to condition on how much to jump by
# This took a long time to execute. I don't see much room for optimization,
# since it's all direct array accesses
with open("./data/day5.txt") as data:
    instructions = [int(n) for n in data.read().split('\n') if n != '']
    instructions_length = len(instructions)
    instruction_index = 0
    steps = 0

    while instruction_index >= 0 and instruction_index < instructions_length:
        steps += 1
        jump = instructions[instruction_index]
        instructions[instruction_index] += -1 if jump >= 3 else 1
        instruction_index += jump

    print("Took {} steps to exit".format(steps))