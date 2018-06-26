# Uses python3

import sys


def explore(adj, x, visited):
    visited[x] = True
    for adj_vertex in adj[x]:
        if not visited[adj_vertex]:
            explore(adj, adj_vertex, visited)
    return


def connected_components(adj, visited):
    # Algorithm to count number of connected components in a graph
    no_of_cc = 0
    for vertex in range(len(adj)):
        if not visited[vertex]:
            explore(adj, vertex, visited)
            no_of_cc += 1
    return no_of_cc


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
    visited = [False] * n
    print(connected_components(adj, visited))


# i/p:
# 4 2
# 1 2
# 3 2
#
# o/p:
# 2
