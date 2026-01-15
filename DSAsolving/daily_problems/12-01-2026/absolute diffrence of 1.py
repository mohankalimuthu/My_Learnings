#https://www.geeksforgeeks.org/problems/absolute-difference-11156/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions


'''
concept Explanation:

1. First, filter elements that are less than k.
   Example: From [7, 98, 56, 43, 45, 23, 12, 8] with k = 54:
   → [7, 43, 45, 23, 12, 8]

2. Then select only the numbers which have two digits.
   → [43, 45, 23, 12, 8]   (Remove 7 and 8)

3. For each two-digit number, check if the absolute difference
   between its digits is exactly 1.

   43 → |4 - 3| = 1
   45 → |4 - 5| = 1
   23 → |2 - 3| = 1
   12 → |1 - 2| = 1
   56 → removed earlier because > k

4. Collect only the numbers that satisfy this condition.

Final Output → [43, 45, 23, 12]

'''

#if this code may you get confused so refer the below code both are same concepts:
def absolute_diff(arr,k):
    res = []
    for i in arr:
        if i>9 and i<k:
            s = str(i)
            if all((abs(int(s[i]) - int(s[i + 1]))) == 1 for i in range(len(s) - 1)):
                res.append(i)
    return res
li = [7, 98, 56, 43, 45, 23, 12, 8]
x = 54
print(absolute_diff(li,x))


'''
Fails for 3-digit numbers like 121 (which should pass)
def absolute_diff(arr,k):
    res = []
    for i in arr:
        if i>9 and i<k:
            s = str(i)
            if abs(int(s[0]) - int(s[1])) == 1:
                res.append(i)
    return res

li = [7, 98, 56, 43, 45, 23, 12, 8]
x = 54
print(absolute_diff(li,x))
'''