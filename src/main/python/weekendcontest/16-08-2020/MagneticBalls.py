from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        min_p = 10 ** 9
        max_p = 1

        for i in position:
            if i <= min_p:
                min_p = i
            if i >= max_p:
                max_p = i
        max_dis = max_p - min_p

        m -= 2
        if m == 0:
            return max_dis
        min_dis = max_dis // (m + 1)
        while min_dis > 1:
            i = min_p
            min_dis_tem = min_dis
            for b in range(m):
                if i + min_dis in position:
                    i += min_dis
                else:
                    min_dis -= 1
                    break
            if min_dis == min_dis_tem:
                return min_dis

        return min_dis


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistance([79, 74, 57, 22], m=4))
