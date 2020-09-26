class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        origin = ['0'] * n
        count = 0
        for i in range(n):
            if ''.join(origin) == target:
                break
            if origin[i] != target[i]:
                count += 1
                for j in range(i, n):
                    origin[j] = str(abs(int(origin[j]) - 1))
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.minFlips('001011101'))
