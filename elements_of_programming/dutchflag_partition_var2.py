import random
import copy
array = [1,3,3,4,2,1,4,2,1,4,4,2]
print(array)

def groupElements(A, keys):
    '''
    `A` (array) - an array containing unordered elements
    `keys` (tuple) - a tuple consisting of 4 keys
    '''

    key_1, key_2, key_3, key_4 = keys

    l_idx, curr_idx = 0, 0
    r_idx, m_idx = len(A)-1, len(A)-1

    while curr_idx < m_idx:
        if A[curr_idx] == key_1:
            # push to leftmost side
            A[curr_idx],A[l_idx] = A[l_idx],A[curr_idx]
            l_idx += 1
            curr_idx += 1

        if A[curr_idx] == key_2:
            # "left middle case", i.e don't do anything, leave it untouched
            curr_idx += 1

        if A[curr_idx] == key_3:
            #swap with the right middle idx
            A[curr_idx],A[m_idx] = A[m_idx],A[curr_idx]
            m_idx -= 1

        else: # A[curr_idx] == key_4:
            A[curr_idx],A[r_idx] = A[r_idx],A[curr_idx]
            r_idx -= 1

    print(l_idx, curr_idx, m_idx, r_idx)
    return A

print(groupElements(array,(1,2,3,4)))
