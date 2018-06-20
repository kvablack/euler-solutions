from itertools import product
from functools import reduce
from operator import mul
from graphviz import Graph

def transform(t):
    # transform (a, b, c, d, e, f) to (b, c, d, e, f, a XOR (b and c))
    return (t[1], t[2], t[3], t[4], t[5], t[0] ^ (t[1] and t[2]))

def ncr(n, r):
    # binomial coefficient
    if n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

def combs(n):
    # calculate number of possibilites for an n-cycle
    return sum(ncr(n - i + 1, i) - ncr(n - i - 1, i - 2) for i in range(n))

inputs = list(product([False, True], repeat=6))

# Generate and render graph of input transformations to observe that they form disjoint cycles
dot = Graph()
for i in range(64):
    dot.node(str(i))
dot.edges((str(inputs.index(p)), str(inputs.index(transform(p)))) for p in inputs)
dot.render('graph')

# Count cycle lengths
cycles = []
while inputs:
    t = inputs.pop()
    n = transform(t)
    length = 1
    while n != t:
        inputs.remove(n)
        n = transform(n)
        length += 1
    cycles.append(length)

# Calculate answer by multiplying together number of possiblities for each cycle
print(reduce(mul, (combs(n) for n in cycles), 1))
