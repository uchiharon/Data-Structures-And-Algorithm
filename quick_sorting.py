

def quick_sort(arr,left,right):
    left = 0
    right = len(arr) - 1
    index = partition(arr, left, right)
    
    if left<index: quick_sort(arr, left, index-1) #Sort left hand side
    if index<right: quick_sort(arr, index, right) #sort right hand side


def partition(arr, left, right):
    pivot = arr[round((left+right)/2)]
    while left <= right: 
        while arr[left] < pivot: left +=1;
        while arr[right] > pivot: left -=1;
        
        if left <= right:
            swap(arr, left, right)
            left +=1
            right -=1
        else:
            swap(arr,left,pivot)
    return left
def swap(arr, left, right):
    arr[left], arr[right] = arr[left], arr[right]
        
value = [3,4,5,2,1,5]
left = 0
right = len(value)-1          
            

quick_sort(value, left, right)
print(value)