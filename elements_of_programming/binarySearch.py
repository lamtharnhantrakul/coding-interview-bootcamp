a = [1,4,7,9,13,16,18,19,20,22,24,27,31,38,55,77,99]
# a = [1,4,7,9,13,16]
def binarySearch(A, val):
    l_idx = 0
    r_idx = len(A)-1

    while l_idx < r_idx:

        m_idx = (l_idx + r_idx) // 2
        print(l_idx, m_idx, r_idx)
        print(A[l_idx], A[m_idx], A[r_idx])
        if val == A[m_idx]:
            return True
        elif val < A[m_idx]:
            r_idx = m_idx - 1  # because we have already checked A[m_idx]
        else: # val > A[m_idx]
            l_idx = m_idx + 1

    return False


print(binarySearch(a, 2))
