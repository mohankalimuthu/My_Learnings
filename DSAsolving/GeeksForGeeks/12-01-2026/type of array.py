#https://www.geeksforgeeks.org/problems/type-of-array4605/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions

'''
solution:
Solution Explanation:

1. If the first element of the array is the minimum value and the last element is the maximum value, return 1.
   This means the array is in ascending order.
   Example: [1, 2, 3, 4, 5] → first = 1 (min), last = 5 (max) → return 1

2. If the first element is the maximum value and the last element is the minimum value, return 2.
   This means the array is in descending order.
   Example: [5, 4, 3, 2, 1] → first = 5 (max), last = 1 (min) → return 2

3. If the first element is less than the last element, return 3.
   This represents a descending rotated array.
   Example: [2, 1, 5, 4, 3] → first = 2, last = 3 → return 3

4. If the first element is greater than the last element, return 4.
   This represents an ascending rotated array.
   Example: [3, 4, 5, 1, 2]
   Explanation of rotation:
   [1, 2, 3, 4, 5] → [2, 3, 4, 5, 1] → [3, 4, 5, 1, 2]

'''

def type_of_array(arr):
    if arr[0] == min(arr) and arr[-1] == max(arr):
        return 1
    if arr[0] == max(arr) and arr[-1] == min(arr):
        return 2
    if arr[0] < arr[-1]:
        return 3
    else:
        return 4

arr = [2, 1, 5, 4, 3]
print(type_of_array(arr))
