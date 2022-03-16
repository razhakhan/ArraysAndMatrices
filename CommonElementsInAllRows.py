def findCommonElements(mat):
    #    initialize 1st row element count as 1
    dic={}
    for i in range(len(mat[0])):
        x=mat[0][i]
        dic[x]=1
    
    # if no. of rows is 1, return 1st row
    if(len(mat)==1):
        arr=[x for x in dic]
        return arr
        
    # increase count of common elements only once for every row using index i    
    ans=[]
    for i in range(1, len(mat)):
        for j in range(len(mat[0])):
            x=mat[i][j]
            if x in dic and dic[x]==i:
                dic[x]+=1
                if(i==len(mat)-1 and dic[x]==len(mat)):
                    ans.append(x)
    return ans
    
t=int(input())
for z in range(t):
    mat=[]
    n,m=map(int, input().split())
    for i in range(n):
        arr=[int(x) for x in input().split()]
        mat.append(arr)
    print(findCommonElements(mat))
