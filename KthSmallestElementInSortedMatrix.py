#User function Template for python3

def cnt(arr, mid, n):
    c=0
    i=n-1 # row
    j=0   # column
    while(i>=0 and j<n):
        x=arr[i][j]
        if(x>mid):
            i-=1
        else:
            c+=(i+1) # all rows before i are less than mid
            j+=1
    return c

def binsearch(arr, n, k):
    l=arr[0][0]
    r=arr[n-1][n-1]
    while(l<=r):
        mid=l+(r-l)//2
        num=cnt(arr, mid, n)
        if(num<k):
            l=mid+1
        else:
            ans=mid
            r=mid-1
    return ans

def kthSmallest(mat, n, k):
    return binsearch(mat, n, k)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()

# } Driver Code Ends


"""

ADDING ELEMENTS TO ARRAY, SORTING IT, AND PRINTING Kth element WAS FASTER ON LEETCODE ( 172 ms ),
WHILE THIS SOLUTION TOOK 307 ms.

Example 1:
Input:
N = 4
mat[][] =     {{16, 28, 60, 64},
                   {22, 41, 63, 91},
                   {27, 50, 87, 93},
                   {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.
 

Example 2:
Input:
N = 4
mat[][] =     {{10, 20, 30, 40}
                   {15, 25, 35, 45}
                   {24, 29, 37, 48}
                   {32, 33, 39, 50}}
K = 7
Output: 30
Explanation: 30 is the 7th smallest element.


"""
