array = [1,88,49,4,12,5,3,2,33,9,7]

def alternateList(A):
    A = sorted(A, reverse=True)

    for i in range(1,len(A),2):
        A[i], A[i+1] = A[i+1], A[i]

    return A

print(alternateList(array))
