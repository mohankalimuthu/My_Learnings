'''
formula:
lower triangle:
row = n
column = 2*(n-j)-1
space = i
print_val = *

upper triangle:
row = n
column = 2*i+1
space = n-i-1
print_val = *
'''


n = 5
for j in range(n):
    for _ in range(j):
        print(" ",end="")
    for _ in range(2*(n-j)-1):
        print("*",end="")
    print()
for i in range(n):
    for _ in range(n-i-1):
        print(" ",end = "")
    for _ in range(2*i+1):
        print("*",end="")
    print()

'''
pattern:
*********
 *******
  *****
   ***
    *
    *
   ***
  *****
 *******
*********

'''