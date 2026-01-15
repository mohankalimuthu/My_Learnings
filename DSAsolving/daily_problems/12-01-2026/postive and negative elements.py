#https://www.geeksforgeeks.org/problems/positive-and-negative-elements4613/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions

'''
Input: arr[] = [-1, 2, -3, 4, -5, 6]
every positive element is followed by a negative element.
Output: [2, -1, 4, -3, 6, -5]
'''

'''
solution:
1. initialize the lists: 'pos','neg','res' as an empty list.
        'pos' will store positive number.
        'neg' will store negative number.
        'res' will store final value
        
2. iterate through the input arr:
        first condition: if iterative element > 0, because want positive after negative
                append the element in 'pos' list.
        second condition: if iterative element < 0 because we want after positive must be negative
                append the element in 'neg' list
3. iterate through the half the length of array: because in 'pos' and 'neg' array value split in half size from the original array
        first append pos value by the respective iterative index
        second append the neg value as same.
     - This ensures every positive number is followed by a negative number.
4. return the res   
'''

def pos_neg(arr):
    pos = []
    neg = []
    res = []
    for i in arr:
        if i>0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(len(arr)//2):
        res.append(pos[i])
        res.append(neg[i])
    return res

li = [-1, 2, -3, 4, -5, 6]
print(pos_neg(li))

