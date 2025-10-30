def movezero(nums):
    zeros=[]
    nonzeros=[]
    for i in nums:
        if i==0:
            zeros.append(i)
        else:
            nonzeros.append(i)
    return nonzeros+zeros

nums = [0, 1, 4, 0, 5, 2]
print(movezero(nums))