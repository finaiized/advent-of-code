# Part 1
"""
First day I attempted to do AoC when the problem was released (9:00 PM). 
Didn't expect too much, but wanted to try it out!

Since I was going for speed, I didn't care too much about code quality.
I intend to go back and implement better solutions so I can learn about the problem,
not just how to hack something together!

I got Rank 243, solved in 10 mins, which isn't bad! Only top 100 get points, but I'm still
getting the hang of things. I always felt solving "interview" coding questions is my weakness,
so I'm trying to improve on that.

I felt this was a pretty easy question. I knew immediately I just had to go through
and see what program (which is what the strings "sdfkjl" are) didn't appear as anyone's children;
therefore, they must be the root. 

The hardest part was probably string parsing properly, while being conscious of any
extra spaces, or newlines that would screw things up. Had a bug where I didn't update the direction
(setting the key instead of dict[key]) that lost be a minute or so.
"""
"""Find the program not supported by anything"""

input_str = open("./data/day7.txt").read()

lines = input_str.split('\n')
visited = dict()
tree_root = None

for line in lines:
    a = line.split(' ')
    name = a[0]

    if name not in visited:
        visited[name] = 0
    else:
        visited[name] += 1

    # separated by columns
    b = line.split(" -> ")
    if len(b) == 1:
        continue

    other_members = b[1].split(',')
    for member in other_members:
        stripped_m = member.strip()
        if stripped_m not in visited:
            visited[stripped_m] = 0
        else:
            visited[stripped_m] += 1

for (key, val) in visited.items():
    if val == 0:
        tree_root = key
        print("Root: {}".format(key))


# Part 2
"""
This part took me a lot longer, like 40 minutes. It shouldn't have been hard, really, but I am
very rusty on tree traversal (I also think I should have some kind of linked list thing ready to go),
and questions like "is the tree balanced" which is what this question is.

I got rank 466, which is lower than I expected.

There's a ton of redundancy in my solution below (multiple traversals for everything),
so it should be fun getting it down into one or two traversals.

Coding the weight of each node was prety simple: node's weight + weight of its children, which is recursive.
Then checking if a node was balanced was much the same: if all of its children have the same weight, it's balanced.

But finding where the imbalance was harder. Actually, pretty simple in the end:

Since we know there is an imbalance (and only one):
- If one of it's children is imbalanced, the problem is higher up the tree, so recursively check there instead.
- If all of it's children is balanced, then one of its children _is_ the imbalance.
"""

lines = input_str.split('\n')
weights = dict()
tree = dict()
for line in lines:
    a = line.split(' ')
    name = a[0]
    weight = int(a[1][1:-1])

    if name not in tree:
        tree[name] = []

    if name not in weights:
        weights[name] = weight

    # separated by columns
    b = line.split(" -> ")
    if len(b) == 1:
        continue

    other_members = b[1].split(',')
    for member in other_members:
        stripped_m = member.strip()
        if stripped_m not in tree:
            tree[stripped_m] = []
        tree[name].append(stripped_m)

def weight(s):
    """Weight of s is the weight of all of its children + itself"""
    if not tree[s]: # Empty, no children
        return weights[s]
    
    children_weight = 0
    for c in tree[s]:
        children_weight += weight(c)
    return weights[s] + children_weight


# All of its children must have the same weight!

# Start at base

def balanced_weight(root):
    if not tree[root]:
        return True # No children = balanced

    # To be balanced, all children must be balanced
    weights = []
    for c in tree[root]:
        weights.append(weight(c))

    # If sum of weights / len is equal to first, must be equal weights

    return sum(weights) // len(weights) == weights[0]

# Navigate tree until we find unbalanced source
def find_imbalance(root):
    if not tree[root]:
        return False

    # If it's balanced, check if it's children are unbalanced. If children are not unabalnced, must not be here
    a = None
    for c in tree[root]:
        if not balanced_weight(c):
            a = c
            break

    if a:
        return find_imbalance(a) # Imbalance not here!

    # Okay, one of my children is imbalanced
    w = []
    for c in tree[root]:
        w.append((c, weight(c)))

    # Which is different?
    for i in range(0, len(w) - 1):
        if w[i][1] != w[i + 1][1]:
            # Different
            heavier = None
            if w[i][1] > w[i + 1][1]:
                heavier = w[i]
            else:
                heavier = w[i + 1]
            
            diff = abs(w[i][1] - w[i + 1][1])
            return weights[heavier[0]] - diff


print(find_imbalance(tree_root))