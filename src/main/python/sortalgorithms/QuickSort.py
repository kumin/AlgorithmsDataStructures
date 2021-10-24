from typing import List


class Solution:
    def quickSort(self, s: int, e: int, a: List[int]) -> None:
        if s >= e:
            return
        p = a[(s+e)//2]
        i = s
        j = e
        while True:
            while a[i] > p:
                i += 1
            while a[j] < p:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        self.quickSort(s, j, a)
        self.quickSort(j + 1, e, a)


if __name__ == '__main__':
    sol = Solution()
    a = [4,2,4,4,2,2,4,2]
    #a = [3, 1, 3, 2, 2]
    sol.quickSort(0, 7, a)
    print(a)
