from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        result = 1
        queue = []
        matrix = [[0 for j in range(n)] for i in range(n)]
        for i in range(len(edges)):
            matrix[edges[i][0]][edges[i][1]] = edges[i][2] + 1
            matrix[edges[i][1]][edges[i][0]] = edges[i][2] + 1
        l = [0] * n
        t = [-1] * n
        t[0] = 0
        queue.insert(0, 0)
        while len(queue) > 0:
            x = queue.pop()
            for i in range(n):
                if t[x] == i:
                    continue
                if matrix[x][i] > 0:
                    if l[x] + matrix[x][i] <= maxMoves:
                        if t[i] == -1:
                            result += matrix[x][i]
                            queue.insert(0, i)
                            t[i] = x
                            l[i] = l[x] + matrix[x][i]
                        else:
                            result += matrix[x][i] -1
                        matrix[x][i] = 0
                        matrix[i][x] = 0
                    else:
                        result += maxMoves - l[x]
                        matrix[i][x] = matrix[x][i] + l[x] - maxMoves
                        matrix[x][i] = 0
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.reachableNodes([[0,2,3],[0,4,4],[2,3,8],[1,3,5],[0,3,9],[3,4,6],[0,1,5],[2,4,6],[1,2,3],[1,4,1]],8,5))
