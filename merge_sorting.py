value = [3,4,5,2,1,5]

for n in value:
    if len(n) > 1:
        for m in range(len(n)-1):
            if n[m] > n[m+1]:
                n[m+1],n[m] = n[m],n[m+1]
        


def merge_sort(value):
    sorter = []

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
    print(sorter)
    