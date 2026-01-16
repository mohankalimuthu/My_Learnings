
'''
formula:
row = n
column = i+1
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

'''    
pattern:
*
**
***
****
*****
'''