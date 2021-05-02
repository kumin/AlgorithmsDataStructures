from typing import List, Dict


class Solution:
    def exchange(self, s, a: List[int]) -> Dict[int, int]:
        n = len(a)
        l = (s + 1) * [0]
        tr = []
        for i in range(1, s + 1):
            for j in range(n):
                if a[j] <= i:
                    if l[i] == 0 or l[i - a[j]] + 1 < l[i]:
                        l[i] = l[i - a[j]] + 1
                        tr.insert(i, j)
        result = {}
        m = s
        while m > 0:
            if tr[m] in result:
                result[tr[m]] = result[tr[m]] + 1
            else:
                result[tr[m]] = 1
            m -= a[tr[m]]

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.exchange(35, [1, 2, 3, 4]))
