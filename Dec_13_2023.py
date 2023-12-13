# 1582. Special Positions in a Binary Matrix
# Easy
# 770
# 29
# Companies
# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:


# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:


# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        import numpy as np
        cnt = 0
        tr_mat = np.array(mat).T
        for i in range(len(mat)):
            if sum(mat[i])==1:
                index = mat[i].index(1)
                if sum(tr_mat[index])==1:
                    cnt += 1
        
        return cnt
        