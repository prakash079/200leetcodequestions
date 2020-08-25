#question-link=https://leetcode.com/problems/minimum-absolute-difference/

----------------------------------------------------------------------------------------
#solution
class Solution:
    '''def min_difference(self,arr:List[int]):
        n=len(arr)
        #arr.sort()
        minimum=arr[0]
        for i in range(n-1):
            if((arr[i+1]-arr[i])<minimum):
                minimum=arr[i]
        return minimum '''
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        #arr.sort()
        minimum=arr[1]-arr[0]
        for i in range(n-1):
            if((arr[i+1]-arr[i])<minimum):
                minimum=arr[i+1]-arr[i]
        ans=[]
        #print(minimum)
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i]==minimum):
                l=[arr[i],arr[i+1]]
                ans.append(l)
        return ans
            
        
        
        
        
