from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        h_max = 0
        s = 0
        s_sub = 0
        height.insert(0, 0)
        height.insert(len(height) - 1, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
