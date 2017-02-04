def partition(A,p,r):
    x = A[r]
    i = p-1
    k = r-1

    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            temp = A[i]
            A[i]=A[j]
            A[j]=temp
    temp2 = A[i+1]
    A[i+1]=A[r]
    A[r]=temp2
    
    return i+1
    
def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

    return A

alist = [2,5,1,6,8,3,5,7]
print(quicksort(alist,0,len(alist)-1))


