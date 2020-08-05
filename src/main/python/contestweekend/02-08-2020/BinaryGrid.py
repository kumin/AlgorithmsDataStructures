from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        le = n - 1
        m = 0
        count = 0
        while le > 0:
            row_index = self.find_satisfied_row(grid, n, m, le)
            if row_index == -1:
                return -1
            else:
                for i in range(row_index, m, -1):
                    temp = grid[i]
                    grid[i] = grid[i - 1]
                    grid[i - 1] = temp
                count += row_index - m
                le -= 1
                m += 1

        return count

    def find_satisfied_row(self, grid: List[List[int]], n: int, m: int, le: int) -> int:
        for i in range(m, n):
            count = 0
            row = grid[i]
            for j in range(n - 1, n - le - 1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
                if count == le:
                    return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
