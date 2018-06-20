import numpy as np

graph = np.zeros((64, 64))
s = 0
for i in range(8):
    n = 2 * i + 1
    for j in range(n - 1):
        graph[s + j][s + j + 1] = 1
        graph[s + j + 1][s + j] = 1
    for v in range(s + 1, s + n, 2):
        graph[v][s - ((n - 2) - (v - s) + 1)] = 1
        graph[s - ((n - 2) - (v - s) + 1)][v] = 1
    s += n


def chromatic(graph, depth):
    if len(graph) == 1:
        print("smallest")
        return 3
    if np.all(np.sum(graph, 0) == np.full((len(graph),), 2)):
        return 2 ** len(graph) + (2 * (-1) ** len(graph))
    for i in range(len(graph)):
        if sum(graph[i]) == 1:
            return 2 * chromatic(np.delete(np.delete(graph, i, 0), i, 1), depth + 1)
    for i in range(len(graph)):
        if sum(graph[i]) == 2:
            v = np.argmax(graph[i])
            g1 = np.copy(graph)
            g2 = np.copy(graph)
            g1[i][v] = 0
            g1[v][i] = 0
            for j in range(len(graph[i])):
                g2[v][j] = max(g2[v][j], g2[i][j])
            g2[v][v] = 0
            g2 = np.delete(np.delete(g2, i, 0), i, 1)
            return chromatic(g1, depth + 1) - chromatic(g2, depth + 1)

print(chromatic(graph, 0))
