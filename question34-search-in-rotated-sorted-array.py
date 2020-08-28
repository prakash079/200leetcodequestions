#question-link=https://leetcode.com/problems/search-in-rotated-sorted-array/

___________________________________________________________________________-
#solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
