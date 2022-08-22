## first solution
def bubble_sort(arr):
    n = len(arr) - 1
    
    for i in range(n):
        for j in range(n):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
        n -= 1
    return arr




def findMedian(arr):
    # Write your code here
    median = 0
    middle = len(arr)//2
    arr = bubble_sort(arr)
    if len(arr)%2 > 0:
        median = arr[middle]
    else:
        median = (arr[median - 1] + arr[median])/2
    return median

print(findMedian([1,4,3]))


## optimal solution

def findMedian(arr):
    # Write your code here
    arr  = sorted(arr)
    middle = len(arr)//2
    
    if len(arr)%2 > 0:
        median = arr[middle]
    else:
        median = (arr[middle] + arr[middle + 1])/2
        
    return median


