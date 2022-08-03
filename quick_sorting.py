value = [3,4,5,2,1,5]

def quick_sort(value):
    left = 0
    right = len(value) - 1
    if 
    print(mid)
    i = 0
    for n in range(mid + 1):
        if value[i] >= value[mid]:
            value[i], value[mid], value[mid-1] = value[mid-1], value[i], value[mid]
            mid -= 1
        else:
            i += 1
            
            

quick_sort(value)
print(value)