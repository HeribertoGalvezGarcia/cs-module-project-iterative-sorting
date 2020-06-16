from typing import Sequence, TypeVar

T = TypeVar('T')


def linear_search(arr: Sequence[T], target: T) -> int:
    for i, item in enumerate(arr):
        if item == target:
            return i

    return -1


def binary_search(arr: Sequence[T], target: T) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if (middle_element := arr[middle]) == target:
            return middle

        if middle_element < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
