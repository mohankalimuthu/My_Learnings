'''
formula:
row = len(s)
column = 0,len(s)-i
space = 0
print_val = s[j]
'''


s = "ABCDE"
for i in range(len(s)):
    for j in range(0,len(s)-i):
        print(s[j],end="")
    print()

'''
pattern:
ABCDE
ABCD
ABC
AB
A
'''