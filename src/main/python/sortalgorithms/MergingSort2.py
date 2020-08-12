from typing import List

from src.main.python.sortalgorithms.AbstractSorting import AbstractSorting


class Merging(AbstractSorting):
    def sort(self, nums: List) -> List:
        if not nums:
            return nums
        n = len(nums)
        start, end = 0, n - 1
        self.merge_sort(nums, start, end)

        return nums

    def merge_sort(self, nums, start, end) -> int:
        if start == end:
            return start

        mid = (start + end) // 2
        self.merge(nums, start, mid, mid + 1, end)

        return nums

    def merge(self, nums: List, s1: int, e1: int, s2: int, e2: int) -> List:
        i, j = e1, e2


if __name__ == '__main__':
    sort = Merging()
    print(sort.sort([0, -1, 100, -5, 2, 4, 67, 4, 4, 4]))
