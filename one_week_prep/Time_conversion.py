## Initial Solution

def timeConversion(s):
    # Write your code here
    temp = s.split(":")
    if "PM" in s:
        if temp[0] != "12":
            temp[0] = str(int(temp[0]) + 12)   
    else:
        if temp[0] == "12":
            temp[0] = "00"
    temp[-1] = temp[-1][:-2]
        
    
    return ":".join(temp)


## First optimal attempt

def timeConversion(s):
    # Write your code here
    temp = s.split(":")
    if "PM" in s and temp[0] != "12":
        temp[0] = str(int(temp[0]) + 12)   
    
    if "AM" in s and temp[0] == "12":
        temp[0] = "00"
    temp[-1] = temp[-1][:-2]
        
    return ":".join(temp)

### Second Optimal solution

def timeConversion(s):
    # Write your code here
    
    if "PM" in s and s[:2] != "12":
        s = str(int(s[:2]) + 12)    + s[2:] 
    if "AM" in s and s[:2] == "12":
        s = "00" + s[2:]      
    return s[:-2]



