'''
formula:
row = len(s)
column = i+1
space = 0
print_val = s[i]
'''

s = "ABCDE"
for i in range(len(s)):
    for j in range(i+1):
        print(s[i],end="")
    print()

''''
pattern:
A
BB
CCC
DDDD
EEEEE
'''
