#Uses python3

import sys
from collections import deque


def bipartite(adj, n):
    color = [-1] * n
    queue = deque([0])  # start with vertex 0
    color[0] = 1

    while queue:
        vertex = queue.popleft()
        for adj_vertex in adj[vertex]:
            if color[adj_vertex] == -1:
                queue.append(adj_vertex)
                color[adj_vertex] = 1 - color[vertex]
            elif color[adj_vertex] == color[vertex]:  # two adjacent vertices have same bipartite value
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj, n))
