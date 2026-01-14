#https://www.geeksforgeeks.org/problems/reverse-sub-array5620/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions

#Input: arr[] = [1, 2, 3, 4, 5, 6, 7], l = 2, r = 4
#Output: [1, 4, 3, 2, 5, 6, 7]
#start from 2 and end with 4 -> 2,3,4 - > reverse it -> 4,3,2 -> put into the original array
#[1,4,3,2,5,6,7]

'''
In the problem description, they mentioned the array is 1-based indexed.
1. So we convert the given left and right values to 0-based index by subtracting 1.
2. Use a while loop to iterate from left to right. Use "left < right" because the right value is always greater than the left value.
3. Swap the element at the left index with the element at the right index.
4. Increment the left pointer and decrement the right pointer after each swap.
5. Return the modified array.
'''

def reverse_subArray(arr,l,r):
    left = l-1
    right = r-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
l = 2
r = 4
print(reverse_subArray(arr,l,r))
