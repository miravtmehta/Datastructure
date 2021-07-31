def binary_search_recursive(data, target, left=0, right=None):
    if right is None:
        right = len(data) - 1
    if left > right:
        return -1

    middle = (left + right) // 2
    if target == data[middle]:
        return middle
    elif target < data[middle]:
        return binary_search_recursive(data, target, left, middle - 1)
    else:
        return binary_search_recursive(data, target, middle + 1, right)


data = [1, 2, 3, 6, 8]
target = 4
print(binary_search_recursive(data, target))
