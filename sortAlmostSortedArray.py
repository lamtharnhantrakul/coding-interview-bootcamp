import heapq
import itertools

array = [3,-1,2,6,4,5,8]

def merge_almost_sorted_array(sequence, k):
    result = []
    min_heap = []

    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence[k:]:
        min_element = heapq.heappushpop(min_heap, x)
        result.append(min_element)

    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result

def merge_almost_sorted_array2(sequence, k):
    '''
    Time complexity is nlog(k). For every n items, we do logk operations (heap characteristic)
    '''
    result = []
    min_heap = []

    # add first k=3 elements to heap
    for x in sequence[:k]:
        heapq.heappush(min_heap, x)

    # progress through the sequence after the first k items
    for x in sequence[k:]:
        min_element = heapq.heappushpop(min_heap, x)
        result.append(min_element)

    # sequentially pop the remaining items in the heap
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result

print(merge_almost_sorted_array(array,3))
print(merge_almost_sorted_array2(array,3))
