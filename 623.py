import operator as op
from functools import reduce

MOD = 1000000007

NCR = [[-1] * 2000 for _ in range(2000)]

def modadd(a, b):
    return ((a % MOD) + (b % MOD)) % MOD

def ncr(n, r):
    global NCR
    if NCR[n][r] == -1:
        r = min(r, n - r)
        numer = reduce(op.mul, range(n, n - r, -1), 1)
        denom = reduce(op.mul, range(1, r + 1), 1)
        NCR[n][r] = numer // denom
    return NCR[n][r]


def stirling(n, k):
    return sum((-1) ** (k - i) * ncr(k, i) * i ** n for i in range(k + 1))

def catalan():
    c = 1
    i = 0
    while True:
        yield int(c)
        c = ((2 * (2 * i + 1)) / (i + 2)) * c
        i += 1

def Lambda(N):
    X = (N - 6) // 3 + 1
    counts = [[0] * N for _ in range(X)]
    cat = catalan()
    for x in range(X):
        terms = next(cat)
        counts[x][x * 3 + 5] = modadd(counts[x][x * 3 + 5], terms)
        for num, i in enumerate(range(x * 3 + 10, N, 5)):
            counts[x][i] = modadd(counts[x][i], terms * stirling(x + 1, num + 2))

    for x in range(X):
        for num, i in enumerate(range(x * 3 + 10, N, 5)):
            g = 2 * x + 1
            counts[x][i] = modadd(counts[x][i], ncr(g, num + 1))

    # for x in range(X):
        # for c in counts[x]:
            # if c != 0:
                # for x2 in range(X);
                    # for c2 in counts[x2]:
                        # 
                        # counts[x + x2 - 1][c + c2 - 1] = modadd(counts[x + x2 - 1][c + c2 - 1], ncr(


    return counts

"""def Lambda(N):
    counts = [[0] * N for _ in range((N - 6) // 3 + 1)]
    cat = catalan()
    for i in range(5, N, 3):
        terms = next(cat)
        counts[i] = modadd(counts[i], terms)
        for num, j in enumerate(range(i + 5, N, 5)):
            x = (i - 5) // 3 + 1
            counts[j] = modadd(counts[j], terms * stirling(x, num + 2))

    for i in range(5, N, 3):
        for num, j in enumerate(range(i + 5, N, 5)):
            g = (i - 5) // 3 * 2 + 1
            counts[j] = modadd(counts[j], ncr(g, num + 1))


    return counts"""

print(Lambda(2000))
