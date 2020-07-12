from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        max_dot = self.product(nums[i], nums[j])
        if n == 2:
            return max_dot
        while i + 1 != j:
            if nums[i] >= nums[j]:
                j = j - 1
                max_dot = max(max_dot, self.product(nums[i], nums[j]))
            else:
                i = i + 1
                max_dot = max(max_dot, self.product(nums[i], nums[j]))
        return max_dot

    def product(self, a, b):
        return (a - 1) * (b-1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([3, 4, 5, 2]))
