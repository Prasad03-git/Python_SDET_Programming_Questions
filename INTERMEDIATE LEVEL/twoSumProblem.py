nums = [-1, -2, -3, -4, -5]
target = -9

# print(nums[1::])
def two_sum_indexs(nums, target):
    seen={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return []


res = two_sum_indexs(nums, target)
print(res)
