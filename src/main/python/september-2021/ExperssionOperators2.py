from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        length = len(num)

        def dfs(start, last_num, result, text):
            if start == length:
                if result == target:
                    ans.append(text)
                return
            if max(1, abs(last_num)) * int(num[start:]) < abs(target - result):
                return
            for i in range(start + 1, length + 1):
                if i - start >= 2 and num_now_str[0] == '0':
                    break
                num_now_str = num[start:i]
                num_now = int(num_now_str)

                if start == 0:
                    dfs(i, num_now, num_now, num_now_str)
                else:
                    dfs(i, num_now, num_now + result, text + '+' + num_now_str)
                    dfs(i, -num_now, -num_now + result, text + '-' + num_now_str)
                    dfs(i, last_num * num_now, result - last_num + last_num * num_now, text + '*' + num_now_str)

        dfs(0, 0, 0, '')
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.addOperators("1000000009", 9))
