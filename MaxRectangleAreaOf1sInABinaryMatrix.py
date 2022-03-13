#User function Template for python3

#function to calculate max area under histogram
def getMaxArea(heights):
        stack = [0]
        heights.append(0)
        ans = 0
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                idx = stack.pop()
                h = heights[idx]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, h * w)
            stack.append(i)
        return ans

class Solution:
    
    def maxArea(self,M, n, m):
        #array to maintain histogram till ith row
        dp=[[0 for i in range(m)] for j in range(n)]
        #copy 1st row as it is
        for j in range(m):
            dp[0][j]=M[0][j]
        #make histogram representation, add 1s from all rows
        for i in range(1, n):
            for j in range(m):
                if(M[i][j]==1):
                    dp[i][j]=M[i][j]+dp[i-1][j]
                else:
                    dp[i][j]=0
        #find max area found of all histograms
        ans=-1
        for i in dp:
            ans=max(ans, getMaxArea(i))
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
    
# This code is contributed 

# } Driver Code Ends

"""
Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.


"""
