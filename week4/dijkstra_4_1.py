#Uses python2

import sys
import Queue   # queue in python 3


class Vertex:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __cmp__(self, other):
        return cmp(self.distance, other.distance)

    def __str__(self):
        return self.index


def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    dist[s] = 0  # distance from source vertex to itself is 0

    pq = Queue.PriorityQueue()   # Known region
    pq.put(Vertex(s, dist[s]))   # Distance of vertex v from source s

    while not pq.empty():
        vertex = pq.get()        # Relax all the outgoing edges of this vertex
        for adj_vertex_index, adj_vertex in enumerate(adj[vertex.index]):
            if dist[adj_vertex] > dist[vertex.index] + cost[vertex.index][adj_vertex_index]:
                dist[adj_vertex] = dist[vertex.index] + cost[vertex.index][adj_vertex_index]
                pq.put(Vertex(adj_vertex, dist[adj_vertex]))

    return -1 if dist[t] == float('inf') else dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
