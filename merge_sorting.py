value = [3,4,5,2,1,5]


def merge_sort(value):
    if len(value) > 1:
        mid = round(len(value)/2)
        left_value = value[:mid]
        right_value = value[mid:]
        
        merge_sort(left_value)
        merge_sort(right_value)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_value) and j < len(right_value):
            if left_value[i] < right_value[j]:
                value[k] = left_value[i]
                i += 1
                k += 1
            else:
                value[k] = right_value[j]
                j += 1
                k += 1
    print(value)

merge_sort(value)
        

        
'''

for n in value:
    if len(n) > 1:
        for m in range(len(n)-1):
            if n[m] > n[m+1]:
                n[m+1],n[m] = n[m],n[m+1]
                
                
    if round(len(value)/2) < 1:
        return value[0]
        
    else:
        for n in range(round(len(value)/2)):
            n*=2
            temp = value[n] + value[n+2]
            for n in range(len(temp) - 1):
                if temp[n] > temp[n+1]:
                    temp[n], temp[n+1] = temp[n + 1], temp[n]
            sorter.append(temp)      
    print(sorter)'''
 