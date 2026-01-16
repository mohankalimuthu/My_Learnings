
'''
formula:
row = 1,n+1
column = 1,i+1
space = 0
print_val = j
'''

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

'''
pattern:
1
12
123
1234
12345
'''