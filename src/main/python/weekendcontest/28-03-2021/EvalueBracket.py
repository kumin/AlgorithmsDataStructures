from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        know_map = {}
        for know in knowledge:
            know_map[know[0]] = know[1]
        bracket = ""
        result = ""
        append = True
        for i in range(0, len(s)):
            if s[i] == "(":
                append = False
            if append:
                result += s[i]
            elif s[i] != "(" and s[i] != ")":
                bracket += s[i]
            if s[i] == ")":
                append = True
                if bracket in know_map:
                    result += know_map[bracket]
                else:
                    result += "?"
                bracket = ""
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))
