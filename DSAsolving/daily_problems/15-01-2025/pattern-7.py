
'''
formula:
row = n
column = 2*i+1
space =n-i-1
print_val = *
'''

n  = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for _ in range(2*i+1):
        print("*",end="")
    print()

'''
pattern:
    *  
   ***
  *****
 *******
*********
'''


