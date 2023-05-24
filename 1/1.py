# https://leetcode.com/problems/two-sum/
# Array, Hash Table
# key: number, value: index


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, num in enumerate(nums):
            if num in map:
                map[num].append(index)
            else:
                map[num] = [index]
        for index, lhs in enumerate(nums):
            rhs = target - lhs
            if lhs == rhs:
                if rhs in map and len(map[rhs]) == 2:
                    result = []
                    result.append(map[lhs][0])
                    result.append(map[rhs][1])
                    return result
            else:
                if rhs in map and map[rhs] != map[lhs]:
                    result = []
                    result.append(map[lhs][0])
                    result.append(map[rhs][0])
                    return result


if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 4], 6))
