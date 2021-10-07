from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        if m * n < len(word):
            return False
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [[False for j in range(m)] for i in range(n)]

        def DFS(x: int, y: int, cur_word: int) -> bool:
            if board[x][y] == word[cur_word]:
                if cur_word == len(word) -1 :
                    return True
                for d in directions:
                    xn = x + d[0]
                    yn = y + d[1]
                    if 0 <= xn < n and 0 <= yn < m and not visited[xn][yn]:
                        visited[xn][yn] = True
                        if DFS(xn, yn, cur_word + 1):
                            return True
                        # back point
                        visited[xn][yn] = False

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word:
                    return True
                visited[i][j] = True
                if DFS(i, j, 0):
                    return True
                visited[i][j] = False


        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
