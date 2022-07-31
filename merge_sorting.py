value = [3,4,5,2,1,5]
def merge_sort(value):
# check if lenght of list is greater than one
    if len(value) > 1:
# split list into two equal half
        mid = round(len(value)/2)
        left_value = value[:mid]
        right_value = value[mid:]
# recusively sort each half
        merge_sort(left_value)
        merge_sort(right_value)
        
        i = 0
        j = 0
        k = 0       
# Merge both halfs
        while i < len(left_value) and j < len(right_value):
            if left_value[i] < right_value[j]:
                value[k] = left_value[i]
                i += 1
            
            else:
                value[k] = right_value[j]
                j += 1
            k += 1           
# Merge remainder
        while i < len(left_value):
            value[k] = left_value[i]
            i += 1
            k += 1
        while j < len(right_value):
            value[k] = right_value[j]
            j += 1
            k += 1
merge_sort(value)
print(value)
 