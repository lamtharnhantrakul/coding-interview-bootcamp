import heapq
sorted_arrays = [[3,5,7],[0,6],[0,6,28]]

def merge_sorted_arrays(sorted_arrays):
    # define min_heap -> keeps track of min_item and the idx of array it came from
    min_heap = []

    # a `list` object is not an `iterator`. Make it an iterator so we can use `next()`
    sorted_arrays_iters = [iter(x) for x in sorted_arrays] # [iter(array1),iter(array2),...]

    # extract the first element from each array
    for i, sorted_array_iter in enumerate(sorted_arrays_iters): # 0, iter(array1)
        first_element = next(sorted_array_iter, None) # we add None, so that `next()` returns None and not a `StopIteration` error
        if first_element is not None:
            heapq.heappush(min_heap,(first_element, i))

    # min_heap now contains the min item of each array
    result = []
    while min_heap:
        min_element, iter_idx = heapq.heappop(min_heap)
        result.append(min_element)
        target_iter = sorted_arrays_iters[iter_idx]
        next_element = next(target_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap,(next_element, iter_idx))
            # note that if `next_element` is None, then that array is empty, and the length of `min_heap` decreases by 1

    return result

def pythonic_merge_sorted_arrays(sorted_arrays):
    print(*sorted_arrays)
    result = heapq.merge(*sorted_arrays)
    return list(result)

print(merge_sorted_arrays(sorted_arrays))
print(pythonic_merge_sorted_arrays(sorted_arrays))
