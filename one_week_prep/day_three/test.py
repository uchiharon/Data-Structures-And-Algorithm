def palindrome(arr):
    if arr == arr[::-1]:
        return 1
    else:
        return 0

def palindromeIndex(s):
    # Write your code here
    if palindrome(s) == 1:
        return -1
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i]  != s[j]:
            if palindrome(s[i+1:j+1]) == 0:
                return j
            else:
                return i
        i += 1
        j -= 1