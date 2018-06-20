def fun(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def findNext(seq):
    return seq[0] if len(set(seq)) == 1 else seq[-1] + findNext([y - x for x, y in zip(seq, seq[1:])])

def findFITS(f):
    l = [f(1)]
    while True:
        m = findNext(l)
        l.append(f(len(l) + 1))
        if m == l[-1]: return
        else: yield m

print(sum(findFITS(fun)))
