class Solution:
    def minOperations(self, n: int) -> int:
        equal_value = (1 + ((n - 1) * 2 + 1)) // 2
        count = 0
        for i in range(n):
            odd = 2 * i + 1
            if odd < equal_value:
                count += equal_value - odd
            else:
                return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations(6))
