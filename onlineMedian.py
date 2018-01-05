sequence = [1,0,3,5,2,0,1]

import heapq

def online_median(sequence):
    min_heap = []
    max_heap = []
    result = []

    for x in sequence:
        val = heapq.heappushpop(min_heap, x)  # push to min heap first, pull out smallest value
        heapq.heappush(max_heap, -val) # add smallest value to max_heap

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))

        if len(max_heap) == len(min_heap):
            result.append(0.5 * (min_heap[0] + (-max_heap[0])))
        else:
            result.append(min_heap[0])

    return result

print(online_median(sequence))
