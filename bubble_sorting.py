import time
a = [3,2,1,5,4,7,9,8]
start = time.time()
for n in a:
    print(a)
    for m in range(len(a) - 1):
        if a[m+1] < a[m]:
            a[m+1], a[m] = a[m], a[m+1]
            
print("new list is:",a,"\nIt took", time.time() - start)