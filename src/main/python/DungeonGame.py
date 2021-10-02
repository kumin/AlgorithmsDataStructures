from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        init_hp = [[0 for i in range(n)] for j in range(m)]
        magic_hp = [[0 for i in range(n)] for j in range(m)]
        if dungeon[0][0] < 0:
            init_hp[0][0] = abs(dungeon[0][0])
        else:
            magic_hp[0][0] = dungeon[0][0]

        def fight(x: int, y: int):
            s = magic_hp[x][y] + dungeon[i][j]
            if s < 0:
                init_hp[i][j] = init_hp[x][y] + abs(s)
                magic_hp[i][j] = 0
            else:
                init_hp[i][j] = init_hp[x][y]
                magic_hp[i][j] = s

        for i in range(0, m):
            for j in range(0, n):
                if i == j == 0:
                    continue
                if i - 1 < 0:
                    fight(i, j - 1)
                elif j - 1 < 0:
                    fight(i - 1, j)
                elif magic_hp[i - 1][j] - init_hp[i - 1][j] > magic_hp[i][j - 1] - init_hp[i][j - 1]:
                    fight(i - 1, j)
                else:
                    fight(i, j - 1)

        print(init_hp)
        print(magic_hp)

        return init_hp[m - 1][n - 1] + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculateMinimumHP([[1, -3, 3], [0, -2, 0], [-3, -3, 0]]))
