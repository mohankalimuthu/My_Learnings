'''
formula:
row = len(s)
column = i+1
space = 0
print_val = s[j]
'''

s = "ABCDE"
for i in range(len(s)):
    for j in range(i+1):
        print(s[j],end = "")
    print()

'''
pattern:
A
AB
ABC
ABCD
ABCDE
'''
