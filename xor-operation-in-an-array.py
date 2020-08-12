#day3
#question7
#question link=https://leetcode.com/problems/xor-operation-in-an-array/

---------------------------------------------------------------------

#solution
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[]
        for i in range(n):
            arr.append(start+(2*i))
        xor=arr[0]
        for i in range(1,n):
            xor=xor^arr[i]
        return xor
