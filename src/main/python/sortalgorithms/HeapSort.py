from typing import List

from src.main.python.sortalgorithms.AbstractSorting import AbstractSorting


class HeapSort(AbstractSorting):
    def sort(self, nums: List) -> List:
        n = len(nums)
        # MakeHeap
        while n > 0:
            for i in range(n // 2 - 1, -1, -1):
                j = i
                index_l = i * 2 + 1
                index_r = i * 2 + 2

                if index_l < n and nums[i] < nums[index_l]:
                    j = index_l

                if index_r < n and nums[j] < nums[index_r]:
                    j = index_r

                if j != i:
                    self.swap(nums, i, j)
            self.swap(nums, 0, n - 1)
            n -= 1
        return nums

    def swap(self, nums: List, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    heap_sort = HeapSort()
    print(heap_sort.sort([2, 1, 3, 4, 5, 6, 7]))
