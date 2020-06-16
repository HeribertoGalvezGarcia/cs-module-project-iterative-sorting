from typing import Sequence, TypeVar, List

T = TypeVar('T')


def selection_sort(arr: Sequence[T]) -> Sequence[T]:
    for i in range(len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


def bubble_sort(arr: Sequence[T]) -> Sequence[T]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr: List[int], maximum: int) -> List[int]:
    maximum += 1
    buckets = [0] * maximum

    for i in arr:
        buckets[i] += 1

    j = 0
    for k in range(maximum):
        for _ in range(buckets[k]):
            arr[j] = k
            j += 1

    return arr


print(counting_sort([1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7))
