from typing import List, Dict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i in range(len(edges)):
            key1 = str(edges[i][0]) + '_' + str(edges[i][1])
            key2 = str(edges[i][1]) + '_' + str(edges[i][2])
            value = succProb[i]
            graph[key1] = value
            graph[key2] = value
        p = []
        for i in range(n):
            p[i] = -1
            key = str(i) + '_' + str(end)
            if key in graph:
                p[i] = graph[key]
        trace = {}

    # def dfs(self, n: int, graph: Dict[str, float], start: int, end: int) -> float:
