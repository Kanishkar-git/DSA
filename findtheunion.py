def union(nums1,nums2):
    union=[]
    for i in nums1+nums2:
        if i not in union:
            union.append(i)
    union.sort()
    return union