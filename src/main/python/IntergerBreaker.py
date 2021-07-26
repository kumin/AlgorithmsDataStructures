class Solution:
    def __init__(self):
        self.muscle = {}

    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 1:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n in self.muscle:
            return self.muscle[n]
        max_dot = max(max(2 * self.integerBreak(n - 2), 2 * (n - 2)), max(3 * self.integerBreak(n - 3), 3 * (n - 3)))
        self.muscle[n] = max_dot
        return max_dot


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerBreak(58))
