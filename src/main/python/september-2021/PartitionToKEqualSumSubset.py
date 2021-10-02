from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        sub_total = total // k
        n = len(nums)
        visited = [False] * len(nums)

        def backTracking(idx: int, g: int, t: int) -> bool:
            if g > k:
                return True
            for i in range(idx, n):
                if visited[i] or nums[i] > t:
                    continue
                t -= nums[i]
                visited[i] = True
                if t == 0:
                    if backTracking(0, g + 1, sub_total):
                        return True
                else:
                    if backTracking(i+1, g, t):
                        return True
                visited[i] = False
                t += nums[i]
            return False

        return backTracking(0, 1, sub_total)


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.canPartitionKSubsets([3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269],
                                 5))
