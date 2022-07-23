import time
# sample list
a = [3,2,1,5,4,7,9,8]
count = len(a) - 1
start = time.time()

# loop through list
for n in range(count):
# Review list current state
    print(a)
# Compare neigboring values
    for m in range(count):
# Monitor number of comparison
        print(m)
        if a[m+1] < a[m]:
            a[m+1], a[m] = a[m], a[m+1]
# Reduce number of comparison since final n value is in the correct position
    count -= 1
            
print("new list is:",a,"\nIt took", time.time() - start)