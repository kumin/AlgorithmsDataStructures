from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        mem = {}
        for i in range(len(nums)):
            for j in range(i-1, -1 , -1):
                diff = nums[i] - nums[j]
                keyj = '{:d}_{:d}'.format(j, diff)
                keyi = '{:d}_{:d}'.format(i, diff)
                if keyj in mem:
                    mem[keyi] = mem[keyj] + 1
                    if mem[keyi] >=3:
                        count += mem[keyi] - 3 + 1
                else:
                    mem[keyi] = 2
            print(mem)
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([7,7,7,7,7]))
