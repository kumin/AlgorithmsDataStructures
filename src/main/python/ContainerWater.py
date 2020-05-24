from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

    def area(self, i, h1, h2):
        return i * min(h1, h2)
