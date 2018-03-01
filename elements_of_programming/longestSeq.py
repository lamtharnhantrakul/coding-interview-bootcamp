array = [1,2,3,4,4,5,3,2,2,2,7,3,3,3,3,3,8,8,8,8,8,8,8,8,8]

def longestSeq2(array):
    '''
    inputs:
    `array` (int array) - array of integers

    returns:
    `max_val` (int) - the value that had the longest sequence
    '''

    # initialize values to keep track of longest sequence
    longest_len = 1 # a single character will always have a `longest_len` of 1
    curr_len = 1
    max_val = None
    prev_val = None

    for val in array:
        if val == prev_val:
            curr_len += 1

            if curr_len > longest_len:
                longest_len = curr_len
                max_val = val

        else: # val != prev_val
            curr_len = 1

        prev_val = val

    return max_val

def longestSeq2(A):
    '''
    inputs:
    `array` (int array) - array of integers

    returns:
    `max_val` (int) - the value that had the longest sequence
    '''

    # initialize values to keep track of longest sequence
    longest_len = 1 # a single character will always have a `longest_len` of 1
    curr_len = 1
    max_val = None

    for i in range(1,len(A)):
        if A[i] == A[i-1]:
            curr_len += 1
            if curr_len > longest_len:
                longest_len = curr_len
                max_val = A[i]
        else: # val != prev_val
            curr_len = 1
    return max_val

print(array)
print(longestSeq2(array))
