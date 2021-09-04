from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        obstacles.sort()
        result = []
        for i in range(0, len(obstacles)):
            max_length = 0
            for j in range(i - 1, -1, -1):
                if obstacles[i] >= obstacles[j] and result[j] > max_length:
                    max_length = result[j]
                    if result[j] == j + 1:
                        break
            result.append(max_length + 1)
        return result
