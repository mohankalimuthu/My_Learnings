'''
row = 1,n+1                 .i
left_ = 1,i+1               .j
print_val = j
space = 2*(n-i)             .k
right = i,0,-1              .l
print_val = l
'''


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(2*(n-i)):
        print(" ",end = "")
    for l in range(i,0,-1):
        print(l,end="")
    print()

'''
pattern:
1        1
12      21
123    321
1234  4321
1234554321
'''