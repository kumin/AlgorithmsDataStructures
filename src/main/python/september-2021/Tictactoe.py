from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return 'Pending'
        matrix = [['c' for i in range(3)] for j in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                matrix[moves[i][0]][moves[i][1]] = 'A'
            else:
                matrix[moves[i][0]][moves[i][1]] = 'B'
        print(matrix)
        for i in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] != 'c':
                return matrix[i][0]

            if matrix[0][i] == matrix[1][i] == matrix[2][i] != 'c':
                return matrix[0][i]

        if matrix[0][0] != 'c' and matrix[0][0] == matrix[1][1] == matrix[2][2]:
            return matrix[0][0]

        if matrix[2][0] != 'c' and matrix[2][0] == matrix[1][1] == matrix[0][2]:
            return matrix[2][0]

        if len(moves) == 9:
            return 'Draw'

        return 'Pending'


if __name__ == '__main__':
    sol = Solution()
    print(sol.tictactoe([[1, 2], [2, 1], [0, 0], [0, 1], [2, 0], [0, 2], [2, 2], [1, 1]]))
