## Initial Solution

def lonelyinteger(a):
    # Write your code here
    count = []
    for i in a:
        if i in count:
            continue
        else:
            if a.count(i) == 1:
                result = i
                break
            else:
                count.append(i)
                
    return result



## First optimal attempt

def lonelyinteger(a):
    # Write your code here
    result = 0
    for i in a:
        result ^= i           
    return result

### Second Optimal solution

