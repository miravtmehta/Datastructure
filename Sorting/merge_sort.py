from random import randint


def create_array(size=5, maxi=50):
    return [randint(0, maxi) for _ in range(size)]


def merge(a, b):
    ta, tb = len(a), len(b)
    orginal = []
    idx_a = 0
    idx_b = 0
    while idx_a < ta and idx_b < tb:
        if a[idx_a] < b[idx_b]:
            orginal.append(a[idx_a])
            idx_a += 1
        else:
            orginal.append(b[idx_b])
            idx_b += 1

    if idx_a < ta:
        orginal.extend(a[idx_a:])
    else:
        orginal.extend(b[idx_b:])

    return orginal


def merge_sort(array):
    if len(array) <= 1:
        return array
    left, right = merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:])
    return merge(left, right)


# array = create_array()
# print(f'unsorted_array', array)

array = [3,2,3,1,2,4,5,5,6]
merged = merge_sort(array)
print(f'sorted_array', merged)