import math
import heapq

with open("p107_network.txt", "r") as f:
    parse = lambda x: 0 if x == "-" else int(x)
    graph = [[parse(x) for x in l.strip().split(",")] for l in f.readlines()]
    heap = [(math.inf, x) for x in range(len(graph))]
    total = int(sum(sum(0 if x == math.inf else x for x in l) for l in graph) / 2)
    
    while len(heap) > 0:
        vc, v = heapq.heappop(heap)
        if vc != math.inf: total -= vc
        for (wc, w), i in zip(heap, range(len(heap))):
            if graph[v][w] < wc:
                heap[i] = (graph[v][w], w)
                heapq._siftdown(heap, 0, i)
    print(total)

        


