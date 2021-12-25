from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        visited = {}
        po = []
        ne = []
        for nu in nums:
            if nu >= 0:
                po.append(nu)
            else:
                ne.append(nu)
        po.sort()
        ne.sort()

        def isVisited(x: int, y: int, z: int) -> bool:
            if (x, y) in visited:
                return True
            if (x, z) in visited:
                return True
            if (y, z) in visited:
                return True
            if (y, x) in visited:
                return True
            if (z, x) in visited:
                return True
            if (z, y) in visited:
                return True

            return False

        def markVisited(x: int, y: int, z: int) -> None:
            visited[(x, y)] = 1
            visited[(x, z)] = 1
            visited[(y, z)] = 1
            visited[(y, x)] = 1
            visited[(z, x)] = 1
            visited[(z, y)] = 1

        for i in range(len(po) - 1):
            for j in range(i + 1, len(po)):
                if isVisited(nums[i], nums[j], 1000000):
                    continue
                for k in range(len(ne)):
                    if abs(nums[k]) > nums[i] + nums[j]:
                        break
                    if abs(nums[k]) < nums[i] + nums[j]:
                        continue
                    if isVisited(nums[i], nums[j], nums[k]):
                        continue
                    result.append([nums[i], nums[j], nums[k]])
                    markVisited(nums[i], nums[j], nums[k])
        print(po, ne)
        for i in range(len(ne) - 1):
            for j in range(i + 1, len(ne)):
                if isVisited(nums[i], nums[j], 1000000):
                    continue
                for k in range(len(po)):
                    print(nums[k], nums[i], nums[j])
                    if nums[k] > abs(nums[i] + nums[j]):
                        break
                    if nums[k] < abs(nums[i] + nums[j]):
                        continue
                    if isVisited(nums[i], nums[j], nums[k]):
                        continue
                    result.append([nums[i], nums[j], nums[k]])
                    markVisited(nums[i], nums[j], nums[k])

        return result
