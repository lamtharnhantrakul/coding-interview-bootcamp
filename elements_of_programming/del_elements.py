A = [4,5,5,5,5,9,10,11,22]
num = 5

def del_number(A, num):
    w_idx = 0

    for i in range(len(A)):
        if A[i] != num:
            A[w_idx] = A[i]
            w_idx += 1
    return w_idx, A

print(del_number(A,num))

def del_duplicates(A):
    w_idx = 1
    for i in range(1, len(A)):
        if A[w_idx - 1] != A[i]:
            A[w_idx] = A[i]
            w_idx += 1 # if this condition is not met, then i increments forwards, but w stays where it is
    return(A)

print(del_duplicates(A))
