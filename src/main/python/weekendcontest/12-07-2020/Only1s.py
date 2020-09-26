class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        st = ''
        for i in range(len(s)):
            if s[i] == '1':
                st = st + s[i]
            if s[i] == '0' or i == len(s) - 1:
                if len(st) > 0:
                    result += int(len(st) * (2 + len(st) - 1) / 2) % (10**9 + 7)
                st = ''

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSub('111000101010111100000'))
