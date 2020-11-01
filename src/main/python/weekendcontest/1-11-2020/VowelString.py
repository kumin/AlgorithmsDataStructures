class Solution:
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.total = 0
        self.sub = ''

    def countVowelStrings(self, n: int) -> int:
        self.backTracking(n)
        return self.total

    def backTracking(self, n: int):
        m = len(self.sub)
        if m < n:
            for vowel in self.vowels:
                if m == 0 or vowel >= self.sub[m - 1]:
                    self.sub += vowel
                    self.backTracking(n)
                    self.sub = self.sub[:-1]
        elif m == n:
            self.total += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.countVowelStrings(43))
