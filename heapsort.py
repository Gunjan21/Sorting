def HeapSort(alist):

    a = []

    def perc_down(a,i):
        done = 0
        size = len(a)
        while not done:
            if i*2>size:
                break
            maxChild = i*2

            if 2*i+1 > size:
                break

            if 2*i+1<size:
                if a[maxChild]<a[2*i+1]:
                    maxChild = i*2 +1

            if a[i]<a[maxChild]:
                print("perc down: swapping")
                temp = a[i]
                a[i]=a[maxChild]
                a[maxChild]=temp
            else:
                break

            i = maxChild
                 
#converting into max heap
    i = len(alist)//2
    while i>0:
        perc_down(alist,i)
        i-=1

    end = len(alist)

    while end>1:

        print('Sorting : swapping',alist[end-1],'and',alist[1])
        temp = alist[end-1]
        alist[end-1]=alist[1]
        alist[1]=temp
        a.append(alist.pop())

        perc_down(alist,1)
        end -= 1

    return a


print("Sorted Max Heap : ", HeapSort([0,3,2,6,9,1,4,7,8]))
    
