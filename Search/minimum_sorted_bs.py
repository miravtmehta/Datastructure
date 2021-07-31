def minimum_search(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] < nums[right]:
            right = middle - 1
        else:
            left = middle
    return nums[left]


data = [0, 1, 6, 7]
print(minimum_search(data))
