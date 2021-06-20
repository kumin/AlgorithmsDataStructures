from typing import List


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        memorial = [[200] * n for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if i == j - 1:
                    memorial[i][j] = self.computeMinAbs(nums[i], nums[j])
                else:
                    tem_min = 200
                    for k in range(i, j):
                        absolute = self.computeMinAbs(nums[j], nums[k])
                        if absolute != -1:
                            tem_min = min(tem_min, absolute)
                    if tem_min == 200:
                        tem_min = -1
                    if memorial[i][j-1] != -1:
                        memorial[i][j] = min(memorial[i][j-1], tem_min)
                    else:
                        memorial[i][j] = tem_min
        result = []
        for i in range(len(queries)):
            result.append(memorial[queries[i][0]][queries[i][1]])

        return result

    def computeMinAbs(self, x, y):
        if x == y:
            return -1
        else:
            return abs(x - y)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDifference([7, 7, 7, 7, 7],
                            [[0, 3], [2, 4], [0, 4], [0, 4], [0, 3]]))
