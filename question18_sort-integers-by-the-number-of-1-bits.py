#question-link=https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

----------------------------------------------------------------------------------_________________________________---------------___________
#solution
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))
        
