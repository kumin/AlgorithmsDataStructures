class Solution:
    def calculate(self, s: str) -> int:
        def infixToPostfix(s: str) -> str:
            r = {"+": 1, "-": 1, "*": 2, "/": 2}
            st = []
            re = ""
            for c in s:
                if c == " ":
                    continue
                if c.isnumeric():
                    re += c
                elif c == "(":
                    st.append(c)
                elif c == ")":
                    c = st.pop()
                    while c != "(":
                        re += c
                        c = st.pop()
                else:
                    re += "|"
                    while len(st) > 0 and r[st[-1]] >= r[c]:
                        re += st.pop()
                    st.append(c)
            if re[-1].isnumeric():
                re += "|"
            for i in range(len(st) - 1, -1, -1):
                re += st[i]
            return re

        def calculatePostfix(s: str) -> int:
            st = []
            n = ""
            for c in s:
                if c.isnumeric():
                    n += c
                elif c == "|":
                    st.append(n)
                    n = ""
                else:
                    a = st.pop()
                    b = st.pop()
                    st.append(str(cal(b, a, c)))
            return int(st[0])

        def cal(a: str, b: str, op: str):
            if op == "+":
                return int(a) + int(b)
            if op == "-":
                return int(a) - int(b)
            if op == "*":
                return int(a) * int(b)
            if op == "/":
                return int(a) // int(b)

        return calculatePostfix(infixToPostfix(s))

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate("3-5 / 2"))
