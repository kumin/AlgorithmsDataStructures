from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        for i in range(0, m - 1):
            for j in range(1, n):
                if points[i][j] < points[i][j - 1] - 1:
                    points[i][j] = points[i][j - 1] - 1
            for j in range(n - 1, -1, -1):
                if j + 1 < n and points[i][j] < points[i][j + 1] - 1:
                    points[i][j] = points[i][j + 1] - 1
                points[i + 1][j] += points[i][j]

        return max(points[m - 1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPoints([[1, 5], [2, 3], [4, 2]]))
