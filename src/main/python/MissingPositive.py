from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_positive = 1
        for num in nums:
            if num == min_positive:
                min_positive += 1
        return min_positive


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([2, 1]))
