#link=https://leetcode.com/problems/partition-labels/

___________________________________________________________________________-
#solution
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right,rightmost[letter])

            if i == right:
                result += [right-left + 1]
                left = i+1

        return result
