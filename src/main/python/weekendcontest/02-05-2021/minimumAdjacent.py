class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        totalSteps = 0
        for i in range(k):
            num, steps = self.findSmallestWonderful(num)
            totalSteps += steps
            print(num + ":" + str(steps))
        return totalSteps

    def findSmallestWonderful(self, num: str) -> ():
        last = 0
        totalSteps = 0
        n = len(num)
        while last < n - 2:
            ok = False
            for i in range(n - 1, last, -1):
                for j in range(i - 1, last, -1):
                    if num[i] > num[j]:
                        num = self.swap(num, j, i)
                        last = j
                        totalSteps += 1
                        ok = True
                        break
                if ok:
                    break
        return num, totalSteps

    def swap(self, num: str, i: int, j: int) -> str:
        tem = num[0:i] + num[j]
        return tem + num[i + 1: j] + num[i] + num[j + 1:len(num)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMinSwaps("5489355142", 4))
