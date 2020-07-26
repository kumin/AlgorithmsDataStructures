from typing import List

class Solution:
    def dijkstra(self, n: int, edges: List[List[int]], weight: List[float], start: int, end: int):
        graph = {}
        for i in range(len(edges)):
            key1 = str(edges[i][0]) + '_' + str(edges[i][1])
            key2 = str(edges[i][1]) + '_' + str(edges[i][2])
            value = weight[i]
            graph[key1] = value
            graph[key2] = value
        p = []
        for i in range(n):
            p[i] = 1000000
            key = str(i) + '_' + str(end)
            if key in graph:
                p[i] = graph[key]
        trace = {}
        queue =[]
        