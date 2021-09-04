class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        result = {}
        substr = ""
        idx = 0
        self.backtracking(result, substr, binary, idx)

        return len(result)

    def backtracking(self, result, substr: str, binary: str, idx: int):
        print(result)
        if idx > len(binary) - 1:
            if len(substr) > 0 and (len(substr) == 1 or substr[0] != "0"):
                result[substr] = 1
            return

        self.backtracking(result, substr, binary, idx + 1)
        substr += binary[idx]
        self.backtracking(result, substr, binary, idx + 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfUniqueGoodSubsequences("001"))
