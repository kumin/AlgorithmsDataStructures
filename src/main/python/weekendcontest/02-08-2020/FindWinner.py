from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            max_value = 0
            for i in range(n):
                if arr[i] > max_value:
                    max_value = arr[i]
            return max_value
        count = 0
        no_win = arr[0]
        while count != k:
            if arr[0] > arr[1]:
                if arr[0] == no_win:
                    count += 1
                else:
                    count = 1
                    no_win = arr[0]
                arr.append(arr[1])
                arr.remove(arr[1])
            else:
                if arr[1] == no_win:
                    count += 1
                else:
                    count = 1
                    no_win = arr[1]
                arr.append(arr[0])
                arr.remove(arr[0])

        return no_win


if __name__ == '__main__':
    sol = Solution()
    print(sol.getWinner([1, 9, 8, 2, 3, 7, 6, 4, 5], 7))
