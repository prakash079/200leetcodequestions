#question9
#link=https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

---------------------------------------------------------------

#solution
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #nums.sort(reverse=True)
        #print(nums)
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(0,len(nums)):
                if(nums[j]<nums[i]):
                    count+=1
            ans.append(count)
            
        return ans
