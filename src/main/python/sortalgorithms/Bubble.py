from typing import List

from src.main.python.sortalgorithms.AbstractSorting import AbstractSorting


class Bubble(AbstractSorting):

    def sort(self, nums: List) -> List:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    tempo = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tempo

        return nums


if __name__ == '__main__':
    sort = Bubble()
    print(sort.sort([0, -1, 100, -5, 2, 4, 67, 4, 4, 4]))
