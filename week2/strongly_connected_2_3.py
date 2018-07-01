#Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj, vertex, visited, topological_order):
    # depth first search algorithm
    
    visited[vertex] = True

    for adj_vertex in adj[vertex]:
        if not visited[adj_vertex]:
            dfs(adj, adj_vertex, visited, topological_order)

    topological_order.append(vertex)


def reverse_graph(adj):
    # Reverse a given graph

    adj_reverse = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            adj_reverse[adj[i][j]].append(i)
    return adj_reverse


def number_of_strongly_connected_components(adj):
    # Algorithm to return number of strongly connected components

    result = 0
    topological_order = []

    visited = [False] * len(adj)

    # get a topological sorted order of vertices & save it in topological_order
    # last element in the topological order has highest value & hence is the source
    for vertex in range(len(adj)):
        if not visited[vertex]:
            dfs(adj, vertex, visited, topological_order)

    # create a reverse of the adj graph
    adj_reverse = reverse_graph(adj)

    visited = [False] * len(adj_reverse)

    # source in adj graph is sink in reverse_adj graph
    # hence pop the elements from the end in topological sorted order
    while topological_order:
        vertex = topological_order.pop()
        if not visited[vertex]:
            dfs(adj_reverse, vertex, visited, [])
            result += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
