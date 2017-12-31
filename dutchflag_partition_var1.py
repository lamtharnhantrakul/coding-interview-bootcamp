import random
import copy
array = [1,2,3,3,3,2,1,3,2,2,2,1,3]
print(array)

def groupElements(A,keys):
    '''
    `A` (array) - an array of size N
    `keys` (tuple) - a tuple containing the keys found in the array
    '''

    key_1, key_2, key_3 = keys

    l_idx = 0
    r_idx = len(A) - 1
    curr_idx = 0

    while curr_idx <= r_idx:
        if A[curr_idx] == key_1:
            # swap the elements and increment the write index in key_1 subarray
            A[curr_idx], A[l_idx] = A[l_idx], A[curr_idx]
            curr_idx += 1
            l_idx += 1

        elif A[curr_idx] == key_2:
            curr_idx += 1
            # leave the element where it is (so it stays in the middle)

        else: # A[curr_idx] == key_3
            # swap the elements and increment the write index in key_3 subarray
            A[curr_idx], A[r_idx] = A[r_idx], A[curr_idx]
            r_idx -= 1

    return A

print(groupElements(array,(1,2,3)))
