from typing import List

from src.main.python.searchalgorithms.AbstractSearching import AbstractSearching


class BinarySearch(AbstractSearching):
    def search(self, nums: List, x: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == x:
                return mid
            if x > nums[mid]:
                l = mid + 1
            elif x < nums[mid]:
                r = mid - 1
        if nums[l] == x:
            return l
        return -1


if __name__ == '__main__':
    searcher = BinarySearch()
    print(searcher.search([1, 2, 36, 75, 100], 100))
