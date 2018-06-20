import math

def expand(node):
    l, x0, y0, x1, y1, t = node

    t_left = t + math.asin(3 / 5)
    l_left = l * (4 / 5)
    h_left = l_left * math.sqrt(2)
    left = (l_left,
            x0 + (l_left * math.cos(t_left)),
            y0 + (l_left * math.sin(t_left)),
            x0 + (h_left * math.cos(t_left - (math.pi / 4))),
            y0 + (h_left * math.sin(t_left - (math.pi / 4))),
            t_left)

    t_right = t - math.asin(4 / 5)
    l_right = l * (3 / 5)
    h_right = l_right * math.sqrt(2)
    right = (l_right,
             x1 + (h_right * math.cos(t_right + (math.pi / 4))),
             y1 + (h_right * math.sin(t_right + (math.pi / 4))),
             x1 + (l_right * math.cos(t_right)),
             y1 + (l_right * math.sin(t_right)),
             t_right)

    return left, right


root = (1, 0, 1, 1, 1, math.pi / 2)  # (length, x0, y0, x1, y1, angle)
rightmost, leftmost, topmost = root, root, root

while True:
    left, right = expand(leftmost)
    if min(left[1], left[3]) < min(right[1], right[3]):
        leftmost = left
    else:
        leftmost = right

    left, right = expand(rightmost)
    if max(left[1], left[3]) > max(right[1], right[3]):
        rightmost = left
    else:
        rightmost = right

    left, right = expand(topmost)
    if max(left[2], left[4]) > max(right[2], right[4]):
        topmost = left
    else:
        topmost = right


    area = (max(rightmost[1], rightmost[3]) - min(leftmost[1], leftmost[3])) * (max(topmost[2], topmost[4]))
    print(area)
