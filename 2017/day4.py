# Part 1
# Easy, about 10 minutes
# The only thing that got me was reading the file:
# The new lines are preserved in line (I thought they'd go away)
# after iterating line-by-line, which messed up the comparision of words
# Also, I forgot to check for empty lines which counted as valid matches

total = 0
with open("./data/day4.txt") as data:
    for line in data:
        stripped_line = line.strip()
        if stripped_line == '':
            break

        words = stripped_line.split(' ')

        seen = set()
        invalid = False
        for word in words:
            if word in seen:
                invalid = True
                break
            else:
                seen.add(word)

        if not invalid:
            total += 1

print("{} passphrases are valid".format(total))

# Part 2
# About 5 minutes
# I briefly considered using a more efficient representation,
# maybe doing something like taking advantage of the ASCII characters
# and build up some index in one pass instead of sorting (O(n) vs O(n log n)),
# ...but nah
total = 0
with open("./data/day4.txt") as data:
    for line in data:
        stripped_line = line.strip()
        if stripped_line == '':
            break

        words = stripped_line.split(' ')

        seen = set()
        invalid = False
        for word in words:
            sorted_word = ''.join(sorted(word)) # Sorts characters and joins the resulting list back into a word
            if sorted_word in seen:
                invalid = True
                break
            else:
                seen.add(sorted_word)

        if not invalid:
            total += 1

print("{} passphrases are valid".format(total))
