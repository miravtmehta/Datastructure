def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == target:
            return middle

        elif target > data[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return -1


data = [1, 2, 3, 6, 8]
target = 8
print(binary_search(data, target))
