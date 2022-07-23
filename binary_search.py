from math import floor

def binary_search(df,value):
    low = 0
    high = len(df) - 1

    while low <= high:
        mid = floor((high + low)/2)
        if df[mid] > value:
            high = mid - 1
            
        else:
            if df[mid] < value:
                low = mid + 1

            else:
                return "YES"
    return "NO"       
text_run = [1,2,3,4,5,6,7,8,9,10]

for a in range(12):
    print(a, binary_search(text_run, a))


