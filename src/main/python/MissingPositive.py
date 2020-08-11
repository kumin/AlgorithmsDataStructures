from typing import List, Dict































































































































































class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        print(nums)
        min_positive = 1
        for num in nums:
            if num <= 0:
                continue
            if num == min_positive:
                min_positive += 1
            elif num != min_positive - 1:
                return min_positive

        return min_positive

    def firstMissingPositive1(self, nums: List[int]) -> int:
        if not nums:
            return 1

        t = type(0.0)

        for i in nums:
            if 0 <= i - 1 < len(nums):
                nums[int(i) - 1] *= 1.0
        i = 0
        while i != len(nums):
            if type(nums[i]) != t:
                return i + 1
            i += 1

        return len(nums) + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([0, 2, 2, 1, 1]))
