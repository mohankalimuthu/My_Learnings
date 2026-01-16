'''
formula:

row = 1,n+1
column = 1,i+1
space = 0
print_val = (i+j+1)%2
'''

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i+j+1)%2,end="")
    print()



'''
pattern:
1
01
101
0101
10101
'''