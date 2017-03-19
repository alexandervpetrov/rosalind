
import math
import heapq

import heap


def shortest_paths(G, W, s):
    """Preconditions: all edges have non-negative weights
    """
    A = {v: math.inf for v in G if v != s}
    A[s] = 0

    h = heap.BinaryMinHeap()
    for v in G:
        h[v] = math.inf
    h[s] = 0

    while h:
        v, v_score = h.extract_min()
        if v_score == math.inf:
            # Graph not connected
            break
        A[v] = v_score
        for u in G[v]:
            if u not in h:
                continue
            u_score = h[u]
            w = W[(v,u)]
            if v_score + w < u_score:
                h[u] = v_score + w

    return A


def shortest_paths_std(G, W, s):
    A = {v: math.inf for v in G if v != s}
    A[s] = 0

    visited = {v: False for v in G}
    h = [(0, s)]
    while h:
        v_score, v = heapq.heappop(h)
        visited[v] = True
        if v_score == math.inf:
            # Graph not connected
            break
        for u in G[v]:
            if visited[u]:
                continue
            w = W[(v,u)]
            if A[v] + w < A[u]:
                A[u] = A[v] + w
                heapq.heappush(h, (A[v] + w, u))

    return A
