from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['']*len(indices)
        for i in range(len(indices)):
            result[indices[i]] = s[i]

        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
