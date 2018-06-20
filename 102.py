def cross(p1, p2):
    return (p1[0] * p2[1] - p1[1] * p2[0]) > 0

def containsOrigin(t):
    p1, p2, p3 = (t[0], t[1]), (t[2], t[3]), (t[4], t[5])
    s1 = (t[2] - t[0], t[3] - t[1])
    s2 = (t[4] - t[2], t[5] - t[3])
    s3 = (t[0] - t[4], t[1] - t[5])

    signs = [cross(*x) for x in [(s1, p1), (s2, p2), (s3, p3)]]
    return len(set(signs)) == 1

with open("p102_triangles.txt", "r") as f:
    triangles = [list(map(int, l)) for l in map(lambda x: x.strip().split(","), f.readlines())]
    print(sum(map(containsOrigin, triangles)))

