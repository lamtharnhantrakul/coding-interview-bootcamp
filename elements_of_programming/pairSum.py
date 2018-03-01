import random
array = [1,3,3,5,7,3,8,2,33,5,1,2,4,23,82,53]
'''
def pairSum(A, k):

    print(A)
    print(k)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i]+A[j] == k:
                print(A[i],A[j])
'''
def quickSort(A):
    if len(A) < 2:
        return A
    else:
        pivot_idx = len(A) // 2
        pivot = A[pivot_idx]
        del A[pivot_idx]

        l_partition = []
        r_partition = []

        for number in A:
            if number < pivot:
                l_partition.append(number)
            elif number > pivot:
                r_partition.append(number)

        return quickSort(l_partition) + [pivot] + quickSort(r_partition)

def pairSum(A, k):
    print(A)
    print(k)

    A.sort()  # O(nlogn) average case
    #A = quickSort(A)
    print(A)
    l_idx = 0
    r_idx = len(A)-1

    while l_idx < r_idx:
        curr_sum = A[l_idx] + A[r_idx]
        if curr_sum == k:
            print(A[l_idx],A[r_idx])
            l_idx += 1
            r_idx += 1
        elif curr_sum < k:
            l_idx += 1
        else: # curr_sum > l
            r_idx -= 1

def pairSum2(A,k):
    if len(A) < 2:
        return "array of length 1, no pair sum possible"

    seen = set() # set containing "seen" unique integers
    unique_output = set() # list containing all possible combinations

    for number in A: # O(n)
        target_pair = k - number
        if target_pair in seen:  # O(1) average case
            unique_output.add((number,target_pair))
        else: # target_pair not in seen
            seen.add(number)

    print(unique_output)

pairSum2(array,9)
