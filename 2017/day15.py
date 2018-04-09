"""
Part One: 10 mins
Part Two: 10 mins

This was a pretty easy question. I needed to check if Python supported arbitrary large numbers
(though with the choice of divisor, I don't think it's even necessary?) and how to do
bit masking. For part 2, I also tried using generators, since it makes a ton of sense there,
and it worked really well.
"""

generatorA = 116
generatorB = 299
generatorA_factor = 16807
generatorB_factor = 48271
divisor = 2147483647

def matching_lower_16_bits(num1, num2):
    return (num1 & 0xFFFF) == (num2 & 0xFFFF)

# Part One
matches = 0
for _ in range(40_000_000):
    generatorA = generatorA * generatorA_factor % divisor
    generatorB = generatorB * generatorB_factor % divisor

    if matching_lower_16_bits(generatorA, generatorB):
        matches += 1

print(f"There are {matches} matches for part 1")

# Part Two
matches = 0

def part2_generatorA():
    generatorA = 116    
    while True:
        generatorA = generatorA * generatorA_factor % divisor
        if generatorA % 4 == 0:
            yield generatorA

def part2_generatorB():
    generatorB = 299    
    while True:
        generatorB = generatorB * generatorB_factor % divisor
        if generatorB % 8 == 0:
            yield generatorB

genA = part2_generatorA()
genB = part2_generatorB()

for _ in range(5_000_000):
    a = next(genA)
    b = next(genB)

    if matching_lower_16_bits(a, b):
        matches += 1

print(f"There are {matches} matches for part 2")        