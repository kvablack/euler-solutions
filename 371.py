from decimal import Decimal

UPPER = 100
total = 0
t0 = 0
t1 = 0
t = 0
complement = 1
for i in range(2, UPPER):
    t = i * (i - 1) * 999 / 2 * ((1000 ** (i - 2) - t0)) - t0
    prob = Decimal(t) / (1000 ** i)
    total += i * complement * prob
    complement *= 1 - prob
    t0 = t1
    t1 = t

print(total)
