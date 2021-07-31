from random import randint


def create_array(size=10, maxi=50):
    return [randint(0, maxi) for _ in range(size)]


def quick_sort(array):
    if len(array) < 1:
        return array
    pivot = array[randint(0, len(array) - 1)]
    small, equal, large = [], [], []
    for x in array:
        if x < pivot:
            small.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            large.append(x)

    return quick_sort(small) + equal + quick_sort(large)


a = create_array()
print(f'unsorted_array', a)
s = quick_sort(a)
print(f'sorted_array', s)

# Best case = N log N
# Worst Case = N * N

# Quick Reads :
# Use randomised quick sort than quick sort to avoid worst case
# https://www.baeldung.com/cs/quicksort-time-complexity-worst-case
"""
Worst case : 
(a)when sorted array choose left most elements : unbalance arrays 
1st half 1 elements and 2nd half with rest
(b)when sorted array and all elements are same
"""
# https://www.youtube.com/watch?v=RFyLsF9y83c&t=205s
