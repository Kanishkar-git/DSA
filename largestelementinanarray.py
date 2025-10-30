def largest_element(arr):
    arr.sort()
    return arr[-1]

# Example
nums = [5, 1, 8, 3, 2]
print(largest_element(nums))  # Output: 8
