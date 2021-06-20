from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        count = 0
        flag = 2
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    queue = [(i, j)]
                    grid2[i][j] = flag
                    ok = True
                    while len(queue) > 0:
                        xy = queue.pop()
                        if grid1[xy[0]][xy[1]] == 0:
                            ok = False
                        for k in range(len(dir)):
                            x = xy[0] + dir[k][0]
                            y = xy[1] + dir[k][1]
                            if 0 <= x < m and 0 <= y < n:
                                if grid2[x][y] == 1:
                                    queue.append((x, y))
                                    grid2[x][y] = flag
                    if ok:
                        count += 1

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubIslands([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                              [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))
