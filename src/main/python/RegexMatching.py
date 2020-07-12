from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for index, num in enumerate(nums):
            if num == target:
                if start == -1:
                    start = index
                else:
                    end = index
            elif num > target:
                break
        if end == -1:
            end = start

        return [start, end]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 5))
