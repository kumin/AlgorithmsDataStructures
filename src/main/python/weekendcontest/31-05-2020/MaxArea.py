from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = 0
        max_w = 0
        for i in range(len(horizontalCuts) - 1):
            max_h = max(max_h, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            max_w = max(max_w, verticalCuts[i + 1] - verticalCuts[i])

        return max_h * max_w


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea(5, 4, [3], [3]))
