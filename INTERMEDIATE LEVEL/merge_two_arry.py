"""
Merge Two Arrays:
For instance, if you have arr1 = {5, 3, 2} and arr2 = {9, 0, 1},
the task is to merge them into one array, resulting in {5, 3, 2, 9, 0, 1}.
"""

arr1 = {5, 3, 2}
arr2 = {9, 0, 1}


def merge_two_arr(arr1, arr2):
    arr = []
    for i in sorted(arr1, reverse=True):
        arr.append(i)
    for i in sorted(arr2, reverse=True):
        arr.append(i)
    print(arr)


merge_two_arr(arr1, arr2)
