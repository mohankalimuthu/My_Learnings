#https://www.geeksforgeeks.org/problems/segregate-even-and-odd-numbers4629/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions


'''
 [12, 34, 45, 9, 8, 90, 3] -> [8, 12, 34, 90, 3, 9, 45]

technique: move even numbers are front side of the array then rest are odd numbers
algo:
1. create empty list for storing odd and even value
2. iterate the input array
3. if: check which values are even
       append in even array
4. else: which values or not even. it means odd
       append in odd array

5. sort both arrays
6. merge even with odd in orginal array
'''

def segregate_odd_even(arr):
    odd = []
    even = []
    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    odd.sort()
    even.sort()
    arr[:] = even + odd   #arr[:] means in-place modification
    return arr

arr = [12, 34, 45, 9, 8, 90, 3]
print(segregate_odd_even(arr))
