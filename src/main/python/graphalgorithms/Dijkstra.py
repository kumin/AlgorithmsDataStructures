from typing import List


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
        visited[start] = True
        trace = {}
        queue = [start]
        while queue:
            u = queue.pop(0)
            for i in range(n):
                key = str(u) + "_" + str(i)
                if key in graph:
                    pathLength = p[u] + graph.get(key)
                    if pathLength < p[i]:
                        p[i] = pathLength
                        trace[i] = u
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
            if u == end:
                break
        if p[end] != self.MAX_WEIGHT:
            v = trace[end]
            path = str(end) + '<-'
            while v != start:
                path = path + str(v) + "<-"
                v = trace[v]
            print(path + str(start))

        return p[end]


if __name__ == '__main__':
    dijkstra = Dijkstra()
    print(
        dijkstra.shortestPath(4, [[0, 1], [0, 3], [0, 2], [1, 3], [2, 3], [1, 2]], [1, 10, 10, 4, 1, 1], 0,
                              2))
