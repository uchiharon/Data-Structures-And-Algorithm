value = [3,4,5,2,1,5]

def quick_sort(value):
    left = 0
    right = len(value) - 1
    index = partition(value, left, right)


def partition(arr, left, right):
    pivot = arr[round((left+right)/2)]
    while left <= right: 
        while arr[left] < pivot: left +=1;
        while arr[right] > pivot: left -=1;
        
        if left <= right:
            swap(arr, left, right)
            left +=1
            right -=1
        
def swap(arr, left, right):
    arr[left], arr[right] = arr[left], arr[right]
        
            
            

quick_sort(value)
print(value)