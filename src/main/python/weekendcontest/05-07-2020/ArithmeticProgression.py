from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        diff = arr[1]-arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    arr = [4, 5, 3, 1, 5, 2, 8, 3]
    solution.canMakeArithmeticProgression(arr)
    print(arr)
