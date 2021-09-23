from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        for i in range(len(arr)):
            arr[i] = ''.join(sorted(arr[i]))
        n = len(arr)
        arr1 = []
        for i in range(n):
            if len(set(arr[i])) != len(arr[i]):
                continue
            arr1.append(arr[i])
        arr = arr1
        n = len(arr)
        if len(arr) == 0:
            return 0

        arr.sort(reverse=True, key=len)
        print(arr)
        l = [0] * len(arr)
        for i in range(n):
            l[i] = len(arr[i])
        for i in range(1, n):
            j_max = -1
            for j in range(0, i):
                if self.isDiff(arr[i], arr[j]) and l[i] < l[j] + len(arr[i]):
                    l[i] = l[j] + len(arr[i])
                    j_max = j

            if j_max != -1:
                arr[i] += arr[j_max]

        return max(l)

    def isDiff(self, s1: str, s2: str) -> bool:
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxLength(["abc", "li", "cu", "ao", "bn"]))
