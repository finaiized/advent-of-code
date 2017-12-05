str = """626	2424	2593	139	2136	163	1689	367	2235	125	2365	924	135	2583	1425	2502
183	149	3794	5221	5520	162	5430	4395	2466	1888	3999	3595	195	181	6188	4863
163	195	512	309	102	175	343	134	401	372	368	321	350	354	183	490
2441	228	250	2710	200	1166	231	2772	1473	2898	2528	2719	1736	249	1796	903
3999	820	3277	3322	2997	1219	1014	170	179	2413	183	3759	3585	2136	3700	188
132	108	262	203	228	104	205	126	69	208	235	311	313	258	110	117
963	1112	1106	50	186	45	154	60	1288	1150	986	232	872	433	48	319
111	1459	98	1624	2234	2528	93	1182	97	583	2813	3139	1792	1512	1326	3227
371	374	459	83	407	460	59	40	42	90	74	163	494	250	488	444
1405	2497	2079	2350	747	1792	2412	2615	89	2332	1363	102	81	2346	122	1356
1496	2782	2257	2258	961	214	219	2998	400	230	2676	3003	2955	254	2250	2707
694	669	951	455	2752	216	1576	3336	251	236	222	2967	3131	3456	1586	1509
170	2453	1707	2017	2230	157	2798	225	1891	945	943	2746	186	206	2678	2156
3632	3786	125	2650	1765	1129	3675	3445	1812	3206	99	105	1922	112	1136	3242
6070	6670	1885	1994	178	230	5857	241	253	5972	7219	252	806	6116	4425	3944
2257	155	734	228	204	2180	175	2277	180	2275	2239	2331	2278	1763	112	2054"""

# Part 1
total = 0
for line in str.split('\n'):
    nums_on_line = line.split('\t')
    nums = [int(n) for n in nums_on_line]
    min_num = min(nums)
    max_num = max(nums)
    diff = max_num - min_num
    total += diff

print("The checksum is {}".format(total))

# Part 2
def evenly_divisble(x, y):
    return x % y == 0 or y % x == 0

def divide_evenly(x, y):
    if x % y == 0:
        return x // y

    return y // x

total = 0
for line in str.split('\n'):
    nums_on_line = line.split('\t')
    nums = [int(n) for n in nums_on_line]
    combinations = [(x, y) for (i, x) in enumerate(nums) for y in nums[i + 1:]]
    evenly_divisible = [divide_evenly(x, y) for (x, y) in combinations if evenly_divisble(x, y)]
    total += sum(evenly_divisible)

print("The checksum is {}".format(total))

"""
# Breakdown

Part 1:
I got this done in about 10-15 minutes, and felt pretty good about the whole way through. I knew
most of the work is just parsing the input, but after that, it was pretty smooth sailing.
I concisously sacrificed some runtime performance by using min/max (going through list twice)
instead of calculating both in one pass for clarity. The only thing that tripped me up is that
the sample input had spaces, and the output had tabs. A quick change to what I split each line
on and I was home free. Originally, I used map() to map characters to numbers, but realized
list comprehensions are more Pythonic.

Part 2:
I knew I had to generate something like (1, 2), (1, 3), (2, 3) for the list [1,2,3],
and it seemed somewhat like a cartesian product that I knew how to do with list comprehensions,
so I managed to calculate the combinations pretty easily. I had a bug the first time around
where it also generated (2, 1), because the second for had as an index a hardcoded 1 instead of
current index + 1.

The one thing that I completely forgot though is that I had to check both x / y and y / x. 
Originally, I was going to add it to my list comprehension, or generate a new one
by reversing nums and redoing the same list comprehension, then realized it would be much
easier (and cleaner) to handle that in a function that checked division both ways.

Time for this part: 15 minutes

Overall: Getting a bit faster, and more confident with my code!
"""