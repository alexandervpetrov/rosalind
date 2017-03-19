
import dijkstra


def test1():
    G = {}
    G[1] = {2, 3}
    G[2] = {3, 4}
    G[3] = {4}
    G[4] = {}
    W = {}
    W[(1,2)] = 1
    W[(1,3)] = 4
    W[(2,3)] = 2
    W[(2,4)] = 6
    W[(3,4)] = 3

    A = dijkstra.shortest_paths(G, W, 1)

    assert A == {1:0, 2:1, 3:3, 4:6}
