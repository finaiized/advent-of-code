"""
Part 1: ~10mins

Didn't do this when it was first released (in fact, doing it on day 8), so had less
time pressure. This was a pretty simple problem: the things that took the longest
was getting the index of the max element (I googled this to look for a one-liner, instead
of using a loop and tracking manually, for future use) and figuring out how to
store distributions so repeats could be detected. You can't store lists in sets,
but you can store a tuple that represents that list. 
Luckily this kind of thing is trivial in Python, if inefficient.
"""

blocks = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
blocks = [int(n) for n in blocks.split('\t')]
block_len = len(blocks)

redistribution_cycles = 0
distribution = set()

while True:
    # Pick biggest block, scanning left-to-right
    max_blocks = max(blocks)
    max_blocks_index = blocks.index(max_blocks)

    # Redistribute
    redistribution_cycles += 1
    blocks[max_blocks_index] = 0
    for i in range(1, max_blocks + 1):
        blocks[(max_blocks_index + i) % block_len] += 1

    # Check if distribution seen before
    if tuple(blocks) in distribution:
        print("Took {} redistribution cycles to reach seen state".format(redistribution_cycles))
        break
    else:
        distribution.add(tuple(blocks))

"""
Part 2: ~3 mins

This was a simple extension, though I tried initially to store a (distribution, cycle)
tuple inside of the set, but then I realized that I couldn't check if another distribution
was in that set since I didn't have cycle. So I just created a separate mapping for that.

By fluke, when I was copy and pasting part of the solution to start part two, I realized
that you can also get the answer by running the same algorithm as in part one AFTER
running it once and using the new block distribution as input (but clearing everything else), 
since when you see it again is precisely how large the cycle is 
(minus 1 since when you reach the same state again, that one doesn't count).
"""

blocks = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
blocks = [int(n) for n in blocks.split('\t')]
block_len = len(blocks)

redistribution_cycles = 0
distribution = set()
distribution_cycles = dict()

while True:
    # Pick biggest block, scanning left-to-right
    max_blocks = max(blocks)
    max_blocks_index = blocks.index(max_blocks)

    # Redistribute
    redistribution_cycles += 1
    blocks[max_blocks_index] = 0
    for i in range(1, max_blocks + 1):
        blocks[(max_blocks_index + i) % block_len] += 1

    # Check if distribution seen before
    if tuple(blocks) in distribution:
        print("Cycles in infinite loop is {}".format(
            redistribution_cycles - distribution_cycles[tuple(blocks)]
        ))
        break
    else:
        distribution.add(tuple(blocks))
        distribution_cycles[tuple(blocks)] = redistribution_cycles