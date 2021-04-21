from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        n = len(boxes)
        for i in range(n):
            step = 0
            for j in range(0, i):
                if boxes[j] == '1':
                    step += i - j
            for j in range(i + 1, n):
                if boxes[j] == '1':
                    step += j - i
            result.append(step)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations("110"))
