class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        unique_sub = []
        s_length = len(s)
        sub_str = ''
        for c in s:
            sub_str += c
            if sub_str not in unique_sub:
                unique_sub.append(sub_str)
                sub_str = ''
            elif s_length % 2 == 0:
                unique_sub[len(unique_sub) - 1] = unique_sub[len(unique_sub) - 1] + sub_str
                sub_str = ''

        return len(unique_sub)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxUniqueSplit('addbsd'))
