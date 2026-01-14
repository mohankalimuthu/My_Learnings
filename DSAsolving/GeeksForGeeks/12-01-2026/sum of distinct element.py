#https://www.geeksforgeeks.org/problems/sum-of-distinct-elements4801/1?page=3&category=Arrays&difficulty=Basic&sortBy=submissions

'''
pd examples:
Examples:
Input: arr[] = [1, 2, 3, 4, 5]
Output: 15
Explanation: Distinct elements are 1, 2, 3, 4, 5. So sum is 15.

Input: arr[] = [5, 5, 5, 5, 5]
Output: 5
Explanation: Only Distinct element is 5. So sum is 5.
'''

'''
solution:
observe the problem sum the distinct element: if any adjacent element is same or repeated value ignore it.

1. so we use set{} dtype first remove repeated distinct element from original array.
2. then use sum() function sum the 'seen' set we get a sum of all distinct value 
'''

def distinct_sum(arr):
    seen = set(arr)
    return sum(seen)

li = [5,5,5,5,5]
print(distinct_sum(li))