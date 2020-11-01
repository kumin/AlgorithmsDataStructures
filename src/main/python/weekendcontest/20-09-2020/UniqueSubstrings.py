class Solution:

    def __init__(self):
        self.unique_substr = []
        self.max_unique_substr = 0

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        self.backtracking(0, s, n)

        return self.max_unique_substr

    def backtracking(self, index: int, s: str, n: int):
        if index == n:
            self.max_unique_substr = max(len(self.unique_substr), self.max_unique_substr)
            return

        sub = ''
        for i in range(index, n):
            sub += s[i]
            if sub not in self.unique_substr:
                self.unique_substr.append(sub)
                self.backtracking(i + 1, s, n)
                print(self.unique_substr)

                self.unique_substr.remove(sub)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxUniqueSplit('addbsd'))
