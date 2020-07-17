from typing import List, Dict


class Dijkstra:
    MAX_WEIGHT = 1000000

    def shortestPath(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i in range(len(edges)):
            key1 = str(edges[i][0]) + '_' + str(edges[i][1])
            key2 = str(edges[i][1]) + '_' + str(edges[i][0])
            value = succProb[i]
            graph[key1] = value
            graph[key2] = value
        p = [self.MAX_WEIGHT] * n
        p[start] = 0
        visited = [False] * n
        trace = {}
        while True:
            u = self.findNearestNode(p, visited)
            if u == end:
                break
            visited[u] = True
            for i in range(n):
                key = str(u) + "_" + str(i)
                if key in graph:
                    pathLength = p[u] + graph.get(key)
                    if pathLength < p[i]:
                        p[i] = pathLength
                        trace[i] = u

        self.printShortestPath(p, trace, start, end)
        return p[end]

    def findNearestNode(self, p: List[float], visited: List[bool]) -> int:
        min = self.MAX_WEIGHT
        for i in range(len(p)):
            if p[i] <= min and not visited[i]:
                min = p[i]
                minNode = i

        return minNode

    def printShortestPath(self, p: List[float], trace: Dict[int, int], start: int, end: int):
        if p[end] != self.MAX_WEIGHT:
            v = trace[end]
            path = str(end) + '<-'
            while v != start:
                path = path + str(v) + "<-"
                v = trace[v]
            print(path + str(start))


if __name__ == '__main__':
    dijkstra = Dijkstra()
    print(
        dijkstra.shortestPath(5, [[0, 1], [0, 3], [0, 2], [2, 3], [1, 2]], [4, 10, 1, 10, 1], 0,
                              4))
