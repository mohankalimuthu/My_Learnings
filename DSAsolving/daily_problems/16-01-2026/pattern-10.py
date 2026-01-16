'''
formula:
Right angle triangle:
row = n
column = i+1
space = 0
print_val = *

inverted Right angle Triangle:
row = n
column = n-i
space = 0
print_val = *
'''

n = 5
for i in range(n):
    for _ in range(i+1):
        print("*",end="")
    print()
for j in range(n):
    for _ in range(n-j):
        print("*",end="")
    print()

'''
pattern:
*
**
***
****
*****
*****
****
***
**
*
'''