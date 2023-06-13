def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    not_in_nums2 = [num for num in set1 if num not in set2]
    not_in_nums1 = [num for num in set2 if num not in set1]
    return [not_in_nums2, not_in_nums1]

# Example usage:
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDifference(nums1, nums2)
print(result)  # Output: [[1, 3], [4, 6]]
