class Solution:
    vowels = ['e', 'u', 'o', 'a', 'i']

    def maxVowels(self, s: str, k: int) -> int:
        max_v = 0
        n = len(s)
        if n == 0:
            return 0
        for i in range(n):
            if i + k <= n:
                max_v = max(max_v, self.countVowels(s[i:i + k]))

        return max_v

    def countVowels(self, s: str):
        count = 0
        for c in s:
            if c in self.vowels:
                count = count + 1
        return count


class Solution1:
    vowels = ['e', 'u', 'o', 'a', 'i']

    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0:
            return 0

        max_v = 0
        current_count = 0
        for i in range(n):
            if s[i] in self.vowels:
                current_count += 1
            if i + 1 > k and s[k - i] in self.vowels:
                current_count -= 1
            if current_count > max_v:
                max_v = current_count

        return max_v


if __name__ == '__main__':
    solution = Solution1()
    print(solution.maxVowels('weallloveyou', 7))
