from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, min(n, i + k + 1)):
                if abs(i - j) <= k and abs(nums[i] - nums[j]) <= t:
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], k=3, t=0))
