class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                d[i][j] = d[i-1][j-1] + 1 if text1[i] == text2[j] else max(d[i][j-1], d[i-1][j])
        return d[len(text1)-1][len(text2)-1]