#question-link=https://leetcode.com/problems/sort-the-matrix-diagonally/

___________________________________________________________________
#solution
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            j_range = range(min(m - i, n))
            diag_mat = sorted(mat[i + j][j] for j in j_range)
            for j in j_range:
                mat[i + j][j] = diag_mat[j]

        for j in range(1, n):
            i_range = range(min(n - j, m))
            diag_mat = sorted(mat[i][i + j] for i in i_range)
            for i in i_range:
                mat[i][i + j] = diag_mat[i]

        return mat
