import time
# sample list
a = [21,4,1,3,9,20,25,6,21,14]
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