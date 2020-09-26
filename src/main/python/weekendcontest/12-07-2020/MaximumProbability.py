from typing import List, Dict


class Solution:
    MIN_PROBABILITY = 0

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i in range(len(edges)):
            key1 = str(edges[i][0]) + '_' + str(edges[i][1])
            key2 = str(edges[i][1]) + '_' + str(edges[i][0])
            value = succProb[i]
            graph[key1] = value
            graph[key2] = value
        p = [self.MIN_PROBABILITY] * n
        p[start] = 1
        visited = [False] * n
        while True:
            u = self.findMaxProbabilityNode(p, visited)
            if u is None or u == end:
                break
            visited[u] = True
            for i in range(n):
                if visited[i]:
                    continue
                key = str(u) + "_" + str(i)
                if key in graph:
                    pathLength = p[u] * graph.get(key)
                    if pathLength > p[i]:
                        p[i] = pathLength

        return p[end]

    def findMaxProbabilityNode(self, p: List[float], visited: List[bool]) -> int:
        min = self.MIN_PROBABILITY
        minNode = None
        for i in range(len(p)):
            if p[i] >= min and not visited[i]:
                min = p[i]
                minNode = i

        return minNode


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
