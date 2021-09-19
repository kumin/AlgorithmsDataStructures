from typing import List


class Solution:
    def __init__(self):
        self.num = ''
        self.target = 0
        self.result = []

    def addOperators(self, num: str, target: int) -> List[str]:
        self.num = num
        self.target = target
        idx = 0
        exp = ''
        self.backtracking(idx, exp)

        print(len(self.result))
        return self.result

    def backtracking(self, idx: int, exp: str):
        if idx > len(self.num) - 1:
            if self.calculate(exp) == self.target:
                self.result.append(exp)
            return
        if exp == '':
            exp += self.num[idx]
            self.backtracking(idx + 1, exp)
        else:
            for m in ['', '-', '+', '*']:
                if len(exp) == 1 and exp[0] == '0' and m == '':
                    continue
                if len(exp) > 1 and not exp[len(exp)-2].isnumeric() and exp[len(exp) -1] == '0' and m == '':
                    continue
                exp1 = exp + m + self.num[idx]
                self.backtracking(idx + 1, exp1)

    def calculate(self, exp: str) -> int:
        stack = []
        i = 0
        while i < len(exp):
            if exp[i].isnumeric():
                idx = self.extractNum(exp, i)
                stack.append(exp[i:idx])
                i = idx
                continue
            if exp[i] == '+' or exp[i] == '-':
                stack.append(exp[i])
                i += 1
                continue
            a = stack.pop()
            i += 1
            idx = self.extractNum(exp, i)
            b = exp[i:idx]
            c = int(a) * int(b)
            stack.append(str(c))
            i = idx
        if len(stack) == 1:
            return int(stack[0])
        i = 1
        cookie = int(stack[0])
        while i < len(stack):
            math = stack[i]
            i += 1
            b = stack[i]
            if math == '+':
                cookie += + int(b)
            else:
                cookie -= int(b)
            i += 1

        return cookie

    def extractNum(self, exp: str, idx: int) -> int:
        while idx < len(exp):
            if exp[idx].isnumeric():
                idx += 1
            else:
                return idx

        return idx


if __name__ == '__main__':
    sol = Solution()
    print(sol.addOperators("1000000009",9))
