def rotated_binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] <= nums[right]:
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        else:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return -1


data = [0]
target = 1
print(rotated_binary_search(data, target))
