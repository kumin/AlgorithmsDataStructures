from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        postfix = self.transformPostfix(s)
        print(postfix)
        stack = []
        for i in range(len(postfix)):
            if postfix[i].isnumeric():
                stack.append(postfix[i])
            else:
                if len(stack) > 1:
                    b = stack.pop()
                    a = stack.pop()
                    c = self.compute(int(a), int(b), postfix[i])
                    stack.append(c)
                else:
                    b = stack.pop()
                    c = self.compute(0, int(b), postfix[i])
                    stack.append(c)

        return stack.pop()

    def compute(self, a: int, b: int, m: str):
        if m == '-':
            return a - b
        else:
            return a + b

    def transformPostfix(self, s: str) -> List[str]:
        s = s.replace(' ', '')
        postfix = []
        stack = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = s[i]
                while i + 1 < len(s) and s[i + 1].isnumeric():
                    i += 1
                    num += s[i]
                postfix.append(num)
            elif s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                c = stack.pop()
                while c != '(':
                    postfix.append(c)
                    c = stack.pop()
            elif s[i] == '+' or s[i] == '-':
                while len(stack) > 0:
                    c = stack[len(stack) - 1]
                    if c == '+' or c == '-':
                        c = stack.pop()
                        postfix.append(c)
                    else:
                        break
                stack.append(s[i])
            i += 1
        while len(stack) > 0:
            postfix.append(stack.pop())
        return postfix


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate("-22+1"))
