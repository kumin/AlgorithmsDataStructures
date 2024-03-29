from typing import List

from src.main.python.sortalgorithms.AbstractSorting import AbstractSorting


class Merging(AbstractSorting):
    def sort(self, nums: List) -> List:
        if not nums:
            return nums
        n = len(nums)
        start, end = 0, n - 1
        return self.merge_sort(nums, start, end)

    def merge_sort(self, nums, start, end) -> List:
        if start == end:
            return [nums[start]]

        mid = (start + end) // 2
        result = self.merge(self.merge_sort(nums, start, mid), self.merge_sort(nums, mid + 1, end))

        return result

    def merge(self, nums1: List, nums2: List) -> List:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        result = []
        while i < n or j < m:
            if j >= m or (i < n and nums1[i] < nums2[j]):
                result.append(nums1[i])
                i += 1
            elif i >= n or (j < m and nums1[i] >= nums2[j]):
                result.append(nums2[j])
                j += 1
        return result


if __name__ == '__main__':
    sort = Merging()
    print(sort.sort([0, -1, 100, -5, 2, 4, 67, 4, 4, 4]))
