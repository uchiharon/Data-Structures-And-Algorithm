# Create list all odd numbers between 1 and a max number
max = input('User insert a number:')
odd_num = []
for a in range(1, int(max)+1):
    if a%2 == 1:
        odd_num.append(a)
print('Odd numbers:',odd_num)

