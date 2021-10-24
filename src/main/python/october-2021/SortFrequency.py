class Solution:
    def frequencySort(self, s: str) -> str:
        f = {}
        cs = []
        for c in s:
            cs.append(c)
            if c in f:
                f[c] += 1
            else:
                f[c] = 1

        def quickSort(s: int, e: int) -> None:
            if s >= e:
                return
            k = (s+e)//2
            p = f[cs[k]]
            i = s
            j = e
            while True:
                while f[cs[i]] > p:
                    i += 1
                while f[cs[j]] < p:
                    j -= 1
                if i >= j:
                    break
                cs[i], cs[j] = cs[j], cs[i]
                j -= 1
                i += 1

            quickSort(s, j)
            quickSort(j + 1, e)

        quickSort(0, len(cs) - 1)
        return ''.join(cs)


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort("acaadcad"))
