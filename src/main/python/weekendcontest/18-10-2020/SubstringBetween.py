class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1
        max_length = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if max_length < j - i - 1:
                        max_length = j - i - 1

        return max_length


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxLengthBetweenEqualCharacters("aa"))
