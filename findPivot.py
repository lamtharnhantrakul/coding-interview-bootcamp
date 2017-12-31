a1 = [9,10,11,12,13,2,3,4,5]
a2 = [11,12,13,2,3,4,5,7,8]
a3 = [11,12,13,14,15,16,17,1,2,3]
a4 = [2,3,4,5,6,7,8]
a5 = [73,85,94,21,27,34,47,54,66]

def findPivot(A):
    # check edge cases

    l_idx = 0
    r_idx = len(A) - 1

    # check edge cases
    if A[l_idx] < A[r_idx]:
        return 0 # array is sorted
    elif A == {} or A == None:
        return -1 # invalid input

    while (l_idx < r_idx):
        m_idx = (l_idx+r_idx)//2
        if A[m_idx] > A[m_idx+1]:
            return m_idx, A[m_idx]

        elif A[m_idx] > A[l_idx]:
            l_idx = m_idx
            '''
            consider A = [2,3,4,5,6]
            This works because if l_idx = 3 and m_idx =3, we go to the other
            else statement making r_idx = 3, which breaks out of the loop
            '''

        else: # A[m_idx] < A[l_idx]
            r_idx = m_idx

    return 0

def findPivot2(A):

    l_idx = 0
    r_idx = len(A) - 1

    while (l_idx < r_idx):
        m_idx = (l_idx+r_idx)//2
        if A[m_idx] > A[m_idx+1]:
            return m_idx, A[m_idx]

        elif A[m_idx] < A[r_idx]:
            r_idx = m_idx
            '''
            consider A = [2,3,4,5,6]
            This works because if l_idx = 3 and m_idx =3, we go to the other
            else statement making r_idx = 3, which breaks out of the loop
            '''

        else: # A[m_idx] < A[l_idx]
            l_idx = m_idx

    return m_idx

print(findPivot(a1))
print(findPivot(a2))
print(findPivot(a3))
print(findPivot(a4))
print(findPivot(a5))
