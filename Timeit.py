import random
from timeit import Timer

def Randomlist(size,length):
    mylist = []
    for i in range(size):
        mylist.append(random.randint(0, length))
    return mylist

Length=[10, 100, 1000, 10000]
Range=[10,100,200,1000]

for i in Length:
    for j in Range:
        mylst = Randomlist(i,j)
        s = 'quickSort(' + str(mylst)+',0,'+'('+str(len(mylst)-1)+')'+ ')'
        t1 = Timer(s, "from Quicksort import quickSort")
        time1 = t1.timeit(3)
        s = 'mergesort(' + str(mylst)+ ')'
        t2 = Timer(s, "from Mergesort import mergesort")
        time2 = t2.timeit(3)
        print('Length=%2d , Range=%2d , Quicksort: %8.6f , Mergesort: %7.6f, percent: %10.2f'%(i,j, time1,time2,time1/time2))

