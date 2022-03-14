"""
Problem Statement
Given an n x n matrix mat[n][n] of integers, find the maximum value of mat[c][d] – mat[a][b] over all choices of indexes such that both c > a and d > b.
Example:-
1 2 3 4 
5 6 7 8
1 9 2 3

In this example, the maximum value is 8 (mat[2][1]-mat[0][0]).

Input:
mat[N][N] = {{ 1, 2, -1, -4, -20 },
             { -8, -3, 4, 2, 1 }, 
             { 3, 8, 6, 1, 3 },
             { -4, -1, 1, 7, -6 },
             { 0, -4, 10, -5, 1 }};
Output: 18
The maximum value is 18 as mat[4][2] 
- mat[1][0] = 18 has maximum difference. 

"""

from sys import maxsize

def maxDifference(mat):
    n=len(mat)
    if(n==1):
        return 0
    
    maxarr=[[0 for i in range(n)] for j in range(n)]
    maxarr[n-1][n-1]=mat[n-1][n-1]
    
    #setting max value for last row
    maxi=mat[n-1][n-1]
    for i in range(n-2, -1, -1):
        if(mat[n-1][i]>maxi):
            maxi=mat[n-1][i]
        maxarr[n-1][i]=maxi
        
    #setting max value for last column
    maxi=mat[n-1][n-1]
    for i in range(n-2, -1, -1):
        if(mat[i][n-1]>maxi):
            maxi=mat[i][n-1]
        maxarr[i][n-1]=maxi
    
    #find the maximum difference, by maintaining a matrix maxarr which stores the max
    #element in the submatrix starting from index [i][j], diff will be huge when 
    #subtracted by max element
    
    ans=-maxsize-1
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if(maxarr[i+1][j+1]-mat[i][j]>ans):
                ans=maxarr[i+1][j+1]-mat[i][j]
            maxarr[i][j]=max(mat[i][j], max(maxarr[i+1][j], maxarr[i][j+1]))
            
    return ans
