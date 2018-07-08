# Uses python2
import math


def union(u, v, nodes):
    set1 = find(u, nodes)
    set2 = find(v, nodes)
    if set1 != set2:
        # make higher indexed node as prent
        if nodes[set1].node_idx > nodes[set2].node_idx:
            nodes[set2].parent = set1
        else:
            nodes[set1].parent = set2
            if nodes[set1].node_idx == nodes[set2].node_idx:
                nodes[set2].node_idx += 1


def find(i, nodes):
    if i != nodes[i].parent :
        nodes[i].parent = find(nodes[i].parent, nodes)
    return nodes[i].parent


def weight(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def make_disjoint_sets(i, nodes, x, y):
    nodes.append(Node(x[i], y[i], i))


def minimum_distance(x, y):
    result = 0.
    n = len(x)

    # create nodes
    nodes = []
    for i in range(n):
        make_disjoint_sets(i, nodes, x, y)

    # crate all possible edges between the nodes
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append(Edge(i, j, weight(x[i], y[i], x[j], y[j])))

    # sort edges in non decreasing order based on edge weight
    edges = sorted(edges, key=lambda edge: edge.weight)

    # Add edge in non decreasing order iff edge does not form a cycle
    # i.e vertices of the edge does not belong to same disjoint set
    for edge in edges:
        if find(edge.u, nodes) != find(edge.v, nodes):
            result += edge.weight
            union(edge.u, edge.v, nodes)
    return result


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.node_idx = 0


if __name__ == '__main__':
    n = int(raw_input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, raw_input().split())
    print("{0:.9f}".format(minimum_distance(x, y)))
