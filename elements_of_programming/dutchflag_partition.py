import random
import copy
array = random.sample(range(1,20),10)

def dutchflag_partition_hanoi(A,p_idx):
    print(A,'original array')
    l_idx = 0
    r_idx = len(A)-1
    curr_idx = 0

    pivot_val = A[p_idx]
    print("pivot_val", pivot_val)

    while curr_idx <= r_idx:
        if A[curr_idx] < pivot_val:
            A[curr_idx] , A[l_idx] = A[l_idx] , A[curr_idx]
            curr_idx += 1
            l_idx += 1
        elif A[curr_idx] == pivot_val:
            curr_idx += 1
        else: #A[curr_idx] > pivot_val
            A[curr_idx] , A[r_idx] = A[r_idx] , A[curr_idx]
            r_idx -= 1
    return A

def dutchflag_partition_correct(A,p_idx):
    print(A,'original array')
    l_idx = 0
    r_idx = len(A)
    curr_idx = 0

    pivot_val = A[p_idx]
    print("pivot_val", pivot_val)

    while curr_idx < r_idx:
        if A[curr_idx] < pivot_val:
            A[curr_idx] , A[l_idx] = A[l_idx] , A[curr_idx]
            curr_idx += 1
            l_idx += 1
        elif A[curr_idx] == pivot_val:
            curr_idx += 1
        else: #A[curr_idx] > pivot_val
            r_idx -= 1
            A[curr_idx] , A[r_idx] = A[r_idx] , A[curr_idx]
    return A


sorted_array_hanoi = dutchflag_partition_hanoi(copy.copy(array), 6)
print(sorted_array_hanoi)
print("-" * 30)
sorted_array_correct = dutchflag_partition_correct(copy.copy(array), 6)
print(sorted_array_correct)
