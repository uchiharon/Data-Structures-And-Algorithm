## Initial Solution

def diagonalDifference(arr):
    # Write your code here
    left = right = 0
    for i in range(len(arr)):
        
        
        left += arr[i][i]
        right += arr[i][-i - 1]
        
    return abs(left - right)

