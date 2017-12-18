"""
I forgot the timings for this one, but part one was pretty simple.
Part two, I just tried to iterate 50 million times, but that took forever,
and takes 2 GB of memory. I caved and looked for a solution, since
I didn't see how to apply the solution from day 16 to it. Turns out,
you just need to note that the index of 0 is ALWAYS 0 (if you insert at 0,
the new value goes to index 1), so you just need to track if anything was
inserted at 0, ending up at 1, and noting that neighbour. You don't need
to keep track of the buffer at all.
"""

buffer = [0]
current_position = 0
STEP = 363

# Part One
for i in range(1, 2017 + 1):
    current_position = (current_position + STEP) % len(buffer)
    buffer.insert(current_position + 1, i)
    current_position += 1

print(buffer[current_position + 1])

zero_pos = 0
neighbour_value = 0
current_position = 0

# Part Two
for i in range(1, 50_000_000 + 1):
    current_position = (current_position + STEP) % i + 1
    if current_position == 1:
        neighbour_value = i

print(neighbour_value)