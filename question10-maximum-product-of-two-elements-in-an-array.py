#day4
#question10
#question link=https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
------------------------------------------

#solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=0
        nums.sort()
        maximum=(nums[-1]-1)*(nums[-2]-1)
        return maximum    
