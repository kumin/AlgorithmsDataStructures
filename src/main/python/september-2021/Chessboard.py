from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        def swapRow(x1: int, x2: int):
            for x in range(x1, x2):
                tem = board[x]
                board[x] = board[x + 1]
                board[x + 1] = tem

        def swapCol(y1: int, y2: int):
            for y in range(y1, y2):
                for i in range(n):
                    tem = board[i][y]
                    board[i][y] = board[i][y + 1]
                    board[i][y + 1] = tem
            self.printMatrix(board)


        def finalChecking() -> bool:
            for i in range(n):
                for j in range(n):
                    if j + 1 < n and board[i][j] == board[i][j + 1]:
                        return False
                    if i + 1 < n and board[i][j] == board[i + 1][j]:
                        return False
            return True

        count = 0
        visited = [False] * n
        for j in range(n):
            if j + 1 < n and board[0][j] == board[0][j + 1]:
                prev = j - 1
                while prev >= 0:
                    if board[0][prev] != board[0][j] and not visited[prev]:
                        break
                    prev -= 1

                next = j + 2
                while next < n:
                    if board[0][next] != board[0][j] and not visited[next]:
                        break
                    next += 1

                if prev < 0 and next >= n:
                    return -1

                if prev >= 0 and (j - prev <= next - j - 1 or next >= n):
                    count += j - prev
                    swapCol(prev, j)
                    visited[j] = True
                    visited[prev] = True
                elif next < n:
                    count += next - j - 1
                    swapCol(j + 1, next)
                    visited[j + 1] = True
                    visited[next] = True
        print(count)
        visited = [False] * n
        for i in range(n):
            if i + 1 < n and board[i][0] == board[i + 1][0]:
                prev = i - 1
                while prev >= 0:
                    if board[prev][0] != board[i][0] and not visited[prev]:
                        break
                    prev -= 1

                next = i + 2
                while next < n:
                    if board[next][0] != board[i][0] and not visited[next]:
                        break
                    next += 1

                if prev < 0 and next >= n:
                    return -1

                if prev >= 0 and (i - prev <= next - i - 1 or next >= n):
                    count += i - prev
                    swapRow(prev, i)
                    visited[i] = True
                    visited[prev] = True
                elif next < n:
                    count += next - i - 1
                    swapRow(i + 1, next)
                    visited[i + 1] = True
                    visited[next] = True
        self.printMatrix(board)
        if not finalChecking():
            return -1
        return count

    def printMatrix(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            print(matrix[i])
        print("-------------")


if __name__ == '__main__':
    sol = Solution()
    print(sol.movesToChessboard([[1, 0, 0, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 1], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]))
