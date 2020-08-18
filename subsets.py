#day6
#question16
#question-link=https://leetcode.com/problems/subsets/
----------------------------------------------------------------------------
#solution
class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
