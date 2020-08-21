#question-link=https://leetcode.com/problems/trapping-rain-water/

-----------------------------------------------------------------------------------

#solution
class Solution:
    def trap(self, height: List[int]) -> int:
        sm=0
        for i in range(1,len(height)):
            sm+=(min(max(height[:i+1]),max(height[i:]))-height[i])
        return sm
