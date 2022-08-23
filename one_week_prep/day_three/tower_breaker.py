def towerBreakers(n, m):
    # Write your code here
    
    if n == 1:
        return 1
    if m == 1:
        return 2
    if n%2 == 1:
        return 1
    else:
        return 2