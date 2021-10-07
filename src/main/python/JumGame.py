from typing import List
from heapq import heappop, heappush


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        visited = [False] * n
        visited[0] = True
        p = 0
        while True:
            max_jum = p + nums[p]
            max_jum_i = p
            for i in range(p + 1, p + nums[p] + 1):
                if nums[p] < i - p:
                    break
                if visited[i]:
                    continue
                if i == n - 1 or nums[i] >= n - 1 - i:
                    return True
                visited[i] = True
                if nums[i] + i >= max_jum:
                    max_jum = nums[i] + i
                    max_jum_i = i
            if max_jum_i > p:
                p = max_jum_i
            else:
                return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump([1, 1, 2, 2, 0, 1, 1]))
