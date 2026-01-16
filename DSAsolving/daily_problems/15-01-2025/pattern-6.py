'''
formula:
row = n
column = 1,n-i+1
space = 0
print_val = j
'''


n = 5
for i in range(n):
    for j in range(1,n-i+1):
        print(j,end="")
    print()


'''
pattern:
12345
1234
123
12
1
'''