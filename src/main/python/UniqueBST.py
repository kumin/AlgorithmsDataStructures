class Solution:
    def numTrees(self, n: int) -> int:
        return self.fn(n)

    def fn(self, i: int) -> int:
        if i == 0 or i == 1:
            return 1
        result = 0
        for j in range(1, i+1):
            result += self.fn(i - j) * self.fn(j - 1)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(4))
