def quick_sort(arr,left,right):
    if left<right:
        index = partition(arr, left, right)
        quick_sort(arr, left, index-1) #Sort left hand side
        quick_sort(arr, index+1, right) #sort right hand side
def partition(arr, left, right):
    i =left
    j = right -1
    pivot = right
    while i < j: 
        while i<right and arr[i] < arr[pivot]: i +=1;
        while j>left and arr[j] >= arr[pivot]: j -=1;
        if i < j:
            swap(arr, left, right)        
    if arr[i] > arr[pivot]:
        swap(arr,i,pivot)
    return i
def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]
############################Testing##########################       
        
value = [3,4,5,2,1,5]         
            
quick_sort(value, 0, len(value)-1)
print(value)