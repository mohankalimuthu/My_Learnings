#https://www.geeksforgeeks.org/problems/maximum-triplet-sum-in-array0129/1?page=4&category=Arrays&difficulty=Basic&sortBy=submissions
'''
mind-blowing trick here used:
example: [5,1,3,2,4]
we want maximum sum of triplest, we know always maximum value is last element of sorted array, same for maximum sum of triplets, last 3 values of sorted array
so sort the array in reverse order: [5,4,3,2,1]
sum of first 3 elements: sum(5,4,3) - > 12 
'''


def max_triplet(arr):
    arr.sort(reverse=True)
    return sum(arr[:3])

li  = [4,2,7,9]
print(max_triplet(li))