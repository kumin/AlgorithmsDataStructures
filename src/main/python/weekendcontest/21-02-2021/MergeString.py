class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m, i, j = len(word1), len(word2), 0, 0
        mStr = ''
        while i < n or j < m:
            if i < n:
                mStr += word1[i]
            if j < m:
                mStr += word2[i]
            i += 1
            j += 1

        return mStr


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeAlternately("ab", "pqrs"))