from functools import reduce


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        a = [ord(c) - ord('a') for c in s]
        mod = 2 ** 63 - 1

        def find(l: int):
            p = pow(26, l, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, a[:l], 0)
            print(cur)
            seen = {cur}
            for i in range(l, len(s)):
                cur = (cur * 26 + a[i] - a[i - l] * p) % mod
                if cur in seen:
                    return i - l + 1
                seen.add(cur)

        res, lo, hi = 0, 0, len(s)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            pos = find(mid)
            if pos:
                lo = mid
                res = pos
            else:
                hi = mid - 1
        return s[res:res + lo]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestDupSubstring("banana"))
