class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        pl = s[0]
        n = len(s)

        for i in range(len(s)):
            pt = s[i]
            l1 = i - 1
            l2 = i + 1
            while l1 >= 0 and l2 <= n - 1:
                if s[l1] == s[l2]:
                    pt = s[l1] + pt + s[l2]
                    l1 -= 1
                    l2 += 1
                else:
                    break
            if len(pt) > len(pl):
                pl = pt

            pt = ""
            l1 = i
            l2 = i + 1
            while l1 >= 0 and l2 <= n - 1:
                if s[l1] == s[l2]:
                    pt = s[l1] + pt + s[l2]
                    l1 -= 1
                    l2 += 1
                else:
                    break
            if len(pt) > len(pl):
                pl = pt
        return pl


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("cbbd"))
