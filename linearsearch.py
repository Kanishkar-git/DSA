def linearsearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

nums = [2, -4, 4, 0, 10]
target = 10
print(linearsearch(nums,target))