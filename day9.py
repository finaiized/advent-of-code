puzzle_input = open("./data/day9.txt").read()

"""
Part 1: ~10 mins

I was writing an exam at 9 PM yesterday (whose idea was that?), so I didn't get to chance
to do this puzzle when it first came out. That's probably a good thing; I'm not sure
I enjoy the thrill of solving the puzzle quickly compared to solving it neatly.

Anyhow, this problem was fairly easy, though being careful of the order of operations
was a bit tricky. You need to check if there was an ignored character first,
then garbage, and finally groups if you're not in garbage.

Another way you can solve this (by Peter Norvig) is to transform the input string
by removing cancelled characters and then everything that is garbage. All that
your left with then is the braces, which you can count easily. That simplifies
things a lot, at the cost of multiple passes through the input.
"""
def stream_score(input_str):
    total_score = 0
    group_score = 0
    in_garbage = False
    next_token_cancelled = False

    for char in input_str:
        if next_token_cancelled:
            next_token_cancelled = False
            continue

        if char == '!':
            next_token_cancelled = True
        elif char == '<':
            in_garbage = True
        elif char == '>':
            in_garbage = False
        elif not in_garbage:
            if char == '{':
                group_score += 1
            elif char == '}':
                total_score += group_score        
                group_score -= 1

    return total_score

assert stream_score("{}") == 1
assert stream_score("{{{}}}") == 6
assert stream_score("{{},{}}") == 5
assert stream_score("{{{},{},{{}}}}") == 16
assert stream_score("{<a>,<a>,<a>,<a>}") == 1
assert stream_score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert stream_score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert stream_score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

print("Total score: {}".format(stream_score(puzzle_input)))

"""
Part 2: ~5 mins

Another fairly basic part 2, though it surfaced a "bug" in my part one program.
Basically, the '<' character is ignored when we're already in garbage,
but my previous program didn't take that into account (and didn't need to, functionally).
After that, it was just counting how many characters were in the garbage section
that weren't cancelled or actual delimiters.
"""
def garbage_count(input_str):
    in_garbage = False
    next_token_cancelled = False
    garbage_count = 0

    for char in input_str:
        if next_token_cancelled:
            next_token_cancelled = False
            continue

        if char == '!':
            next_token_cancelled = True
        elif char == '<' and not in_garbage:
            in_garbage = True
        elif char == '>':
            in_garbage = False
        elif in_garbage:
            garbage_count += 1

    return garbage_count

assert garbage_count("<>") == 0
assert garbage_count("<xcvbert>") == 7
assert garbage_count("<<<<>") == 3
assert garbage_count("<{!>}>") == 2
assert garbage_count("<!!>") == 0
assert garbage_count("<!!!>>") == 0
assert garbage_count("<{o'i!a,<{i<a>") == 10

print("Garbage count: {}".format(garbage_count(puzzle_input)))