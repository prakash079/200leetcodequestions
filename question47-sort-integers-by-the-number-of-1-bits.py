#link-https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

------------------------------------------------------------------------------------------
#solution
class Solution:
    def sortByBits(self, arr: List[int]):
        return sorted(arr, key = lambda x: (bin(x).count('1'), x))
