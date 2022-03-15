
#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,arr, n): 
        
        #transpose
        for i in range(n):
            for j in range(i, n):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
                
        #reverse rows        
        i=0
        j=n-1
        while(i<j):
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
            
    #Function to rotate matrix clockwise by 90 degrees.
    def rotateby90clockwise(self,arr, n): 
        
        # transpose
        for i in range(n):
            for j in range(i, n):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        
        # reverse columns        
        for k in range(n):
            i=0
            j=n-1
            while(i<j):
                arr[k][i], arr[k][j] = arr[k][j], arr[k][i]
                i+=1
                j-=1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends


"""

Input:
N = 3 
matrix[][] = {{1, 2, 3},
              {4, 5, 6}
              {7, 8, 9}}
Output: 
Rotated Matrix:
3 6 9
2 5 8
1 4 7

"""
