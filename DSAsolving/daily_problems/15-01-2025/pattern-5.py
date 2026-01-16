'''
formula:
row = n
column = i,n
space = 0
print_val = *
'''


n = 5
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()


'''
pattern:
*****
****
***
**
*
'''