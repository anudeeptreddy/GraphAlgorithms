# Uses python3

import sys


def reach(adj, x, y, visited):
    # Algorithm to verify if y can be reached from x in a undirected graph
    visited[x] = True
    if x == y:
        return 1
    for adj_vertex in adj[x]:
        if not visited[adj_vertex]:
            if reach(adj, adj_vertex, y, visited):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [False] * n
    print(reach(adj, x, y, visited))


# i/p:
# 4 4
# 1 2
# 3 2
# 4 3
# 1 4
# 1 4
#
# o/p:
# 1
