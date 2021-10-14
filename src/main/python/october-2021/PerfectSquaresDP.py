import math


class Solution:
    def numSquares(self, n: int) -> int:
        s = [n+1]*(n+1)
        s[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                s[i] = min(s[i], s[i - j*j] + 1)

        return s[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(200))