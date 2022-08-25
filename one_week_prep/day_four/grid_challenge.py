def gridChallenge(grid):
    # Write your code here
    lenght = len(grid)
    for i in range(lenght):
        grid[i] = sorted(grid[i])
        
    for j in range(len(grid[0])):  
        for i in range (lenght-1):
            if ord(grid[i][j]) > ord(grid[i+1][j]):
                return 'NO'
        
    return "YES"