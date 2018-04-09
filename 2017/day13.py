"""
This one took a long time for various reasons. I didn't track exactly how long it took,
but I estimate part one took about 20 minutes, and part two took an hour.

There's not much to say about part one, so let's skip to part two.
In theory, part two isn't much of a change: add a delay, then simulate.
But it took a looong time, so I didn't know if I had a bug in my program
or something else. Originally, I used a dictionary mapping for layers:
the depth of the layer as the key, and the range of the layer as the value
(some layers don't exist, so I was a bit lazy to use an array with null values).
I thought this was the source of a bottleneck, so I re-wrote both parts to use
arrays instead, and while performance increased slightly, I still didn't get any
answers when in iteration 10 000, which took a solid 5 minutes.

Now I wasn't sure what iteration it was suppose to be exactly, but after some
sleuthing online, I saw that people got answers in the 3 million range (since
puzzle input is unique, seeing the answer doesn't spoil the problem). Okay,
I would clearly be waiting for hours to get to that.

That's when it hit me: the algorithm I was using was O(n^2). Basically,
every iteration, I was starting from scratch, delaying n picoseconds,
then running the packet through and seeing if it was detected. However,
I didn't need to replay from the beginning each time: if I saved the initial state
after the delay (where the simulation of scanners move, but the packet doesn't),
then I would only have to simulate one extra time step to reach the start state
of the next delay, turning it into O(n) essentially! This was much, much faster
(for reference, since the delay is in the 3 millions, 3 000 000^2 is 9 trillion),
though it still took a good while to do.
"""
input_str = open("./data/day13.txt").read()

layers_dict = [i.split(": ") for i in input_str.split('\n')]
layers_dict = {int(n): int(d) for n, d in layers_dict} # {layer: depth}
max_depth = max(layers_dict.keys()) + 1 # + 1 so if max_depth = 6, we want to access indexes [0, 6]

layers = [None] * max_depth
for i in range(max_depth):
    if i in layers_dict:
        layers[i] = layers_dict[i]

def step(layers, scanner_positions, scanner_directions):
    """Moves the scanner's positions one step forward.
    
    Modifies positions and possibly directions in place.
    """
    # Advance all scanners one step, reversing direction if it hits the end    
    for scanner in range(max_depth):
        if layers[scanner] is not None:
            scanner_positions[scanner] += scanner_directions[scanner]
            if scanner_positions[scanner] >= layers[scanner] - 1 or scanner_positions[scanner] <= 0:
                scanner_directions[scanner] *= -1

# Part One
def severity(layers):
    current_position = -1
    total_severity = 0
    scanner_positions = [0] * max_depth
    scanner_directions = [1] * max_depth

    for i in range(max_depth):
        # Move packet forward
        current_position += 1

        # Check if there is a scanner at this position (always 0). If so, it is caught.
        if layers[current_position] is not None and scanner_positions[current_position] == 0:
            severity = current_position * layers[current_position]
            total_severity += severity
        
        # Advance all scanners one step, reversing direction if it hits the end    
        step(layers, scanner_positions, scanner_directions)

    return total_severity

print(f"The severity of the trip is {severity(layers)}")

# Part Two
def delay_to_avoid_detection(layers):
    delay = 0

    # Old scanner positions/directions. Every update,
    # we advance one step to reach the new initial state,
    # to avoid having to simulate to this point again
    prev_scanner_positions = [0] * max_depth
    prev_scanner_directions = [1] * max_depth

    while True:
        current_position = -1
        scanner_positions = prev_scanner_positions[:]
        scanner_directions = prev_scanner_directions[:]
        caught = False

        if delay % 10000 == 0:
            print(f"Testing {delay}...")

        # Simulate travel through the firewall
        for j in range(max_depth):
            # Move packet forward
            current_position += 1

            # Check if there is a scanner at this position (always 0). If so, it is caught.
            if layers[current_position] is not None and scanner_positions[current_position] == 0:
                caught = True
                break
                
            # Advance all scanners one step, reversing direction if it hits the end    
            step(layers, scanner_positions, scanner_directions)
        
        if not caught:
            return delay

        # Advance all scanners one step, reversing direction if it hits the end    
        step(layers, scanner_positions, scanner_directions)

        delay += 1
    

print(f"Delaying {delay_to_avoid_detection(layers)} picoseconds causes the packet to not be caught!")
