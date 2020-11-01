from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        previous = 0
        for i in range(len(pieces)):
            for k in range(len(pieces[i])):
                piece = pieces[i][k]
                if piece in arr:
                    if k == 0:
                        previous = arr.index(piece)
                    else:
                        if previous + 1 != arr.index(piece):
                            return False
                        else:
                            previous += 1
                else:
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFormArray([49, 18, 16], [[16, 18, 49]]))
