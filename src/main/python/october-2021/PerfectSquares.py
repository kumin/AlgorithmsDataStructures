import math


class Solution:
    def __init__(self):
        self.cookie = {}

    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if self.isPerfectSquare(n):
            return 1
        result = n
        for i in range(1, n//2+1):
            print(i)
            if n - i in self.cookie:
                r1 = self.cookie[n - i]
            else:
                r1 = self.numSquares(n - i)
                self.cookie[n - i] = r1
            if i in self.cookie:
                r2 = self.cookie[i]
            else:
                r2 = self.numSquares(i)
                self.cookie[i] = r2
            if r1 + r2 < result:
                result = r1 + r2
            if self.isPerfectSquare(n - i) and self.isPerfectSquare(i):
                break
        return result

    def isPerfectSquare(self, n: int) -> bool:
        root = math.sqrt(n)
        return int(root + 0.5) ** 2 == n


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(200))