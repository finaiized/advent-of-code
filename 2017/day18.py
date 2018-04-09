from multiprocessing import Process, Queue

"""
This day was an absolute doozy. Looking at the stats, you could be in the top 100
with both parts completed if you finished it in less than _40_ minutes! That's
really long!

The first part was fine. It was just another instruction processing one, this time
with slightly more instructions. I completed this in 12:17 and got rank 86!!!
I finally got into the top 100! This felt really good, since my goal was to
get in the top 100 at some point.

Part two though... it took me an hour and 10 minutes after to do it, for rank 385.
It definitely should not have taken this long, but for various reasons, it did.

- I had a bug in my part one program, which, looking at Reddit afterwards, so did
a ton of people. The problem is that sometimes the instruction takes a value (integer)
and other times a register (character), but I didn't realize that the jump instruction
took a value in the X position. The test input provided didn't have that, but my
input did. This failed silently, since retrieving an integer from the registers
failed and returned 0 (the default) (this was necessary because by default, all
registers have 0 value, and they may not have been seen yet). I was lucky to look
at the instructions and notice this, because there was no way I could have debugged that.
- I also had a bug with my jump instruction, where after jumping, I incremented
the instruction pointer by 1, instead of leaving it to execute the jumped-to address.
- I wasn't sure how to run the program side-by-side and communicate between them.
I really wished I had Erlang's message passing at this point, but I was stuck with Python
and didn't really know how to use IPC with it. The first thing I did was just to run them
serially, swapping between them whenever one was blocked on a receive. In theory, this
works fine, but it took me a long time for it to work. I had a few deadlock scenarios,
and coupled with the above bugs, it was hard to tell what wasn't working.
- Because of how I named my programs in the code, when the question asked for the
number of times program 1 sent, I thought it was 1-indexed, instead of 0-indexed,
so once I got my serial swapping-back-and-forth implementation working, I
used the value of what would be program 0, giving the wrong answer! Therefore,
I gave up with this approach because I thought it was wrong.
- I ended up caving and scraping the serial implementation for a multi-process one.
This was easier to get working, and probably what I should have done in the first place.
At this point, I had all the bugs in my interpreter fixed, so it was basically just learning
how to pass things back and forth through the queues. The only other thing was that
I didn't know how to detect deadlock, so I didn't: I just printed out all the sends,
and waited for no more output (deadlock), then used those values. Afterwards, I went
back and added a timeout as a way to detect deadlock and end.

The complexity of the recent questions is definitely ramping up! I had a lot of fun
working through them though.
"""

input_str = open("./data/day18.txt").read().split('\n')

def get_value(registers, token):
    """Returns the number in token, or the value in the register named token."""
    try:
        value = int(token)
    except ValueError:
        value = registers.get(token, 0)

    return value

def part_one():
    instruction_pointer = 0
    registers = {}
    last_sound_played = 0

    while True:
        instruction = input_str[instruction_pointer]
        tokens = instruction.split(' ')

        ins = tokens[0]
        token1 = tokens[1]
        token2 = tokens[2] if len(tokens) == 3 else None

        if token1 not in registers:
                registers[token1] = 0

        if ins == "snd":
            last_sound_played = registers[token1]
        elif ins == "set":
            set_value = get_value(registers, token2)
            registers[token1] = set_value
        elif ins == "add":
            add_value = get_value(registers, token2)
            registers[token1] += add_value
        elif ins == "mul":
            mul_value = get_value(registers, token2)
            registers[token1] *= mul_value
        elif ins == "mod":
            mod_value = get_value(registers, token2)
            registers[token1] = registers[token1] % mod_value   
        elif ins == "rcv":
            rcv_value = get_value(registers, token1)
            if rcv_value != 0:
                print(f"Recovered {last_sound_played} for part one")
                break
        elif ins == "jgz":
            j_value = get_value(registers, token1)
            if j_value > 0:
                jump_by = get_value(registers, token2)
                instruction_pointer += jump_by
                continue
        instruction_pointer += 1

def part_two(pid, my_queue, other_queue):
    registers = {'p': pid}
    instruction_pointer = 0
    number_of_sends = 0

    while True:
        instruction = input_str[instruction_pointer]
        tokens = instruction.split(' ')
        ins = tokens[0]
        token1 = tokens[1]
        token2 = tokens[2] if len(tokens) == 3 else None

        if token1 not in registers:
                registers[token1] = 0

        if ins == "snd":
            send_value = get_value(registers, token1)
            other_queue.put(send_value)
            number_of_sends += 1
        elif ins == "set":
            registers[token1] = get_value(registers, token2)
        elif ins == "add":
            add_value = get_value(registers, token2)
            registers[token1] += add_value
        elif ins == "mul":
            mul_value = get_value(registers, token2)
            registers[token1] *= mul_value
        elif ins == "mod":
            mod_value = get_value(registers, token2)
            registers[token1] = registers[token1] % mod_value    
        elif ins == "rcv":
            try:     
                recv_val = my_queue.get(True, 1)
                registers[token1] = recv_val
            except:
                # Deadlock
                print(f"Program {pid} sent {number_of_sends} messages before stopping")
                break
        elif ins == "jgz":
            j_value = get_value(registers, token1)

            if j_value > 0:
                jump_by = get_value(registers, token2)
                instruction_pointer += jump_by
                continue

        instruction_pointer += 1

# Part One
part_one()

# Part Two
q1 = Queue()
q2 = Queue()
p1 = Process(target=part_two, args=(0, q1, q2))
p2 = Process(target=part_two, args=(1, q2, q1))
p1.start()
p2.start()
p2.join()
p1.join()