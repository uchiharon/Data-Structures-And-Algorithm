## using only python inbuilt functions

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    print(sum(arr[:4]), sum(arr[-4:]))


## using manually built functions

def bubble_sort(arr):
    n = len(arr)
    m = n - 1
    for i in range(n):
        
        for j in range(m):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
        m -= 1
    return arr
                           

def miniMaxSum(arr):
    # Write your code here
    arr = bubble_sort(arr)
    minsum = 0
    maxsum = 0
    
    for i in range(4):
        j = i + 1
        
        minsum += arr[i]
        maxsum += arr[-j]
        
    print(minsum, maxsum)


## Optimal solution considering 

def miniMaxSum(arr):
    # Write your code here
    s = 0
    minsum = 10**9
    maxsum = 0
    
    for i in arr:
        minsum = min(i, minsum)
        maxsum = max(i, maxsum)
        s += i 
    print(s - maxsum, s - minsum)