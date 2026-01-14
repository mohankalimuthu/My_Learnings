#https://www.geeksforgeeks.org/problems/count-pair-sum5956/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions

#Input: x = 10, arr1[] = [1, 3, 5, 7], arr2[] = [2, 3, 5, 8]
# arr1   arr2
#  5      5   = 10  - count 1
#  7      3   = 10  - count 2
#Output: 2

'''
solution:
1. create an empty set. named seen
2. initialize a variable 'count' to 0. this will store the total number of valid pairs
3. iterate through arr1:
    for each element calculate (x-element).
    add this value to the seen set
4. iterate through arr2:
    if the current iterative element exists in the 'seen' set,
    increase the count value +1, because we found the valid pair
5. return the count
'''

def count_pairs(arr1,arr2,x):
    seen = set()
    count = 0
    for i in arr1:
        seen.add(x-i)
    for j in arr2:
        if j in seen:
            count+=1
    return count

arr1 = [1,3,5,7]
arr2 = [2,3,5,8]
x = 10
print(count_pairs(arr1,arr2,x))

#tc = O(n)