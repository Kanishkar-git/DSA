def second_largest(arr):
    arr = list(set(arr))   # remove duplicates
    arr.sort()
    return arr[-2]         # second last element

# Example
nums = [5, 1, 8, 3, 8, 2]
print(second_largest(nums))  # Output: 5
