INFINITY = 999999999

def merge(A,p,q,r):
    #n1 = q-p+1
    #n2 = r-q
    L = A[p:q+1]
    R = A[q+1:r+1]
    print("merge called : A = ", A)
    print("merge called : L = ", L, ", R = ", R)
    print(" p = ", p, ", q = ", q, " , r = ", r)
    L.append(INFINITY)
    R.append(INFINITY)
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
            

def mergesort(A,p,r):
    if p<r:
        print("mergesort: A = ", A, ", p = ", p, " , r = ", r)
        q = (p+r)//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
    return A

alist = [5,3,8,2,6,9,1,7]
blist = [1,2,3,4,5,6,7]
clist = [2]
print(mergesort(alist,0,len(alist)-1))
#print(mergesort(blist,0,len(blist)-1))
#print(mergesort(clist,0,len(alist)-1))

