#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c):
        dx=[0, 1, 0, -1]
        dy=[1, 0, -1, 0]
        di=0
        xi=0
        yi=0
        ans=[]
        visited=[ [0 for i in range(c)] for j in range(r) ]
        
        for i in range(r*c):
            ans.append(matrix[xi][yi])
            visited[xi][yi]=1
            xi=xi+dx[di]
            yi=yi+dy[di]
            if(xi>=0 and xi<r and yi>=0 and yi<c and visited[xi][yi]==0):
                pass
            else:
                xi=xi-dx[di]
                yi=yi-dy[di]
                di=(di+1)%4
                xi=xi+dx[di]
                yi=yi+dy[di]
        return ans
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
