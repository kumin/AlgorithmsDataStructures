from typing import List
from heapq import heappop, heappush


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        p = 0
        while p < n:
            if p == n - 1 or nums[p] + p >= n - 1:
                return True
            i = p + 1
            next_p = p
            while i <= nums[p] + p:
                if nums[i] + i > nums[p] + p:
                    next_p = i
                    break
                i += 1
            if next_p == p:
                return False
            p = next_p


if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump([1, 1, 2, 2, 0, 1, 1]))
