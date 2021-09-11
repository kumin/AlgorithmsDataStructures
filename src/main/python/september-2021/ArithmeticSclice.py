from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        subnums = []
        diff = 0
        for i in range(len(nums)):
            subnums.append(nums[i])
            count += self.backTracking(diff, i + 1, subnums, nums)
            subnums.pop()
        return count

    def backTracking(self, diff, idx: int, subnums: List[int], nums: List[int]) -> int:
        count = 0
        if idx == len(nums):
            return count
        if len(subnums) >= 2:
            if nums[idx] - subnums[len(subnums) - 1] == diff:
                subnums.append(nums[idx])
                count += 1
                count += self.backTracking(diff, idx + 1, subnums, nums)
                subnums.pop()
        else:
            subnums.append(nums[idx])
            diff = subnums[1] - subnums[0]
            count += self.backTracking(diff, idx + 1, subnums, nums)
            subnums.pop()
        count += self.backTracking(diff, idx + 1, subnums, nums)
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
