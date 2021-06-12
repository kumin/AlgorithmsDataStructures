class Solution:
    def __init__(self, n: int, metrix: [[]]):
        self.n = n
        self.visited = [False] * n
        self.metrix = metrix

    def findIslands(self):
        m = self.n + 2
        self.metrix.insert(0, [1] * self.n)
        self.metrix.append([1] * self.n)
        for row in self.metrix:
            row.insert(0, 1)
            row.append(1)
        queue = [[0, 0]]
        self.metrix[0][0] = 2
        while len(queue) > 0:
            node = queue.pop(0)
            if node[1] + 1 < m and self.metrix[node[0]][node[1] + 1] == 1:
                queue.append([node[0], node[1] + 1])
                self.metrix[node[0]][node[1] + 1] = 2
            if node[1] - 1 >= 0 and self.metrix[node[0]][node[1] - 1] == 1:
                queue.append([node[0], node[1] - 1])
                self.metrix[node[0]][node[1] - 1] = 2
            if node[0] + 1 < m and self.metrix[node[0] + 1][node[1]] == 1:
                queue.append([node[0] + 1, node[1]])
                self.metrix[node[0] + 1][node[1]] = 2
            if node[0] - 1 >= 0 and self.metrix[node[0] - 1][node[1]] == 1:
                queue.append([node[0] - 1, node[1]])
                self.metrix[node[0] - 1][node[1]] = 2
        self.printMatrix()

    def printMatrix(self):
        for row in self.metrix:
            print(row)

    def dfs(self, x):
        for i, v in enumerate(self.metrix[x]):
            if self.visited[i]:
                continue
            if v == 1:
                self.visited[i] = True
                self.dfs(i)


if __name__ == '__main__':
    sol = Solution(6,
                   [[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 1]])
    sol.findIslands()
