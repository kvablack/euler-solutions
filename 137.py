# http://math.caltech.edu/~syye/teaching/courses/Ma8_2015/Lecture%20Notes/ma8_wk10.pdf
# http://www.wolframalpha.com/input/?i=inverse+of++x%2F(1-x-x%5E2)


# integer solutions of x to 5x^2 + 2x + 1 = y^2 are golden nuggets
# https://www.alpertron.com.ar/JQUAD.HTM
# this particular form has infinite solutions, which are found among the convergents of the continued fraction representation of the roots of 5x^2 - 1 = 0
# the roots are +- sqrt(1/5)
# the continued fraction of those roots is +- [0; 2, 4, 4, 4, 4, ...]

n1 = [0, 1]
d1 = [1, 2]
for i in range(100):
    n1.append(4 * n1[-1] + n1[-2])
    d1.append(4 * d1[-1] + d1[-2])

n2 = [0, 1]
d2 = [1, -2]
for i in range(100):
    n2.append(-4 * n2[-1] + n2[-2])
    d2.append(-4 * d2[-1] + d2[-2])

import math

def is_square(i):
    return not (math.sqrt(i) - int(math.sqrt(i)))

def golden_nuggets(n):
    num = 0
    x = 2
    while num < n:
        m = math.sqrt(5 * (x**2) - 4)
        m1 = (-1 - m) / 5.0
        m2 = (-1 + m) / 5.0
        if m1.is_integer() and m1 > 0:
            num += 1
            yield int(m1), x
        elif m2.is_integer() and m2 > 0:
            num += 1
            yield int(m2), x
        x += 1

print(is_square(5 * (74049690**2) + 2 * 74049690 + 1))
print(list(golden_nuggets(5)))
        
