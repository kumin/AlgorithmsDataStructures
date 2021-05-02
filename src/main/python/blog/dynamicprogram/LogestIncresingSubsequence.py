from typing import List


class Solution:
    def findSlopes(self, a: List[int]) -> List[int]:
        n = len(a)
        if n == 0 or n == 1:
            return a
        trace = {0: -1}
        l = [0]
        d = 0
        for i in range(1, n):
            if a[i] <= a[l[0]]:
                l[0] = i
                trace[i] = -1
            elif a[i] >= a[l[d]]:
                trace[i] = l[d]
                d += 1
                l.append(i)
            else:
                t = self.binarySearch(a, l, a[i])
                trace[i] = l[t - 1]
                l[t] = i

        i = l[d]
        result = []
        while i != -1:
            result.insert(0, a[i])
            i = trace[i]
        return result

    def binarySearch(self, a: List[int], l: List[int], x: int) -> int:
        b = 0
        e = len(l)

        while b < e:
            p = (b + e) // 2
            if x <= a[l[p]]:
                e = p - 1
                if x > a[l[p - 1]]:
                    return p
            elif x > a[l[p]]:
                b = p + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSlopes([1, 2, 8, 3, 10, 5, 9, 3, 3, 6, 7]))
