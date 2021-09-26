from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return 0
        queue = [[0, 0, 0, 0]]
        grid[0][0] = -1
        l = {}
        l['0_0'] = [0, 0, 0, 0]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        min_length = m * n
        while len(queue) > 0:
            pot = queue.pop()
            for d in direction:
                x = pot[0] + d[0]
                y = pot[1] + d[1]
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1 and pot[2] < k:
                        queue.insert(0, [x, y, pot[2] + 1, pot[3] + 1])
                        l['{}_{}'.format(x, y)] = [x, y, pot[2] + 1, pot[3] + 1]
                        grid[x][y] = -2
                    elif grid[x][y] == 0:
                        if x == m - 1 and y == n - 1:
                            if pot[3] + 1 < min_length:
                                min_length = pot[3] + 1
                        else:
                            queue.insert(0, [x, y, pot[2], pot[3] + 1])
                            l['{}_{}'.format(x, y)] = [x, y, pot[2], pot[3] + 1]
                            grid[x][y] = -1
                    elif grid[x][y] == -1:
                        lxy = l['{}_{}'.format(x, y)]
                        if lxy[2] > pot[2]:
                            queue.insert(0, [x, y, pot[2], pot[3] + 1])
                            l['{}_{}'.format(x, y)] = [x, y, pot[2], pot[3] + 1]

        return min_length if min_length < m * n else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPath([[0, 1, 0, 0, 0, 1, 0, 0],
                            [0, 1, 0, 1, 0, 1, 0, 1],
                            [0, 0, 0, 1, 0, 0, 1, 0]]
                           , 1))
