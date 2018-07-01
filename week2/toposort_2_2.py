#Uses python3

import sys


def dfs(adj, used, order, vertex):
    used[vertex] = 1
    for adj_vertex in adj[vertex]:
        if not used[adj_vertex]:
            dfs(adj, used, order, adj_vertex)
    order.append(vertex)


def toposort(adj):
    # Algorithm to find an order consistent with all the dependencies
    used = [0] * len(adj)
    order = []

    for vertex in range(len(adj)):
        if not used[vertex]:
            dfs(adj, used, order, vertex)
    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

