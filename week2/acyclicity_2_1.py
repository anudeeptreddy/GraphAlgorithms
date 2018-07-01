#Uses python3

import sys


def dfs(adj, vertex, visited, path):
    # Return True if a directed graph has a cycle

    if visited[vertex]:  # since we test all output paths, it suffices to test each node only once
        return False

    visited[vertex] = True
    path[vertex] = True

    for adj_vertex in adj[vertex]:
        if path[adj_vertex] or dfs(adj, adj_vertex, visited, path):
            return True
    path[vertex] = False
    return False


def acyclic(adj):
    # Algorithm to detect cycle in a directed graph
    visited = [False] * len(adj)
    path = [False] * len(adj)
    for vertex in range(len(adj)):
        if dfs(adj, vertex, visited, path):
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))


# i/p:
# 4 4
# 1 2
# 4 1
# 2 3
# 3 1

# o/p:
# 1


