from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            m = i % 2
            if m == nums[i] % 2:
                i += 1
                continue
            for j in range(i + 1, len(nums)):
                if j % 2 != nums[j] % 2 and nums[j]%2 == m:
                    break
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
            i += 1

        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParityII([648, 831, 560, 986, 192, 424, 997, 829, 897, 843]))
