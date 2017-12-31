A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

def rotateMatrixC(A):
    for i in range(len(A) // 2):
        for j in range(i, (len(A)-1) -i):
            A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]
    return A

def rotateMatrixCC(A):
    for i in range(len(A) // 2):
        for j in range(i, (len(A)-1) -i):
            A[i][j], A[j][~i], A[~i][~j], A[~j][i] = A[j][~i], A[~i][~j], A[~j][i], A[i][j]
    return A

def reflectMatrixVert(A):
    for col in range(len(A) // 2):
        for row in range(len(A)):
            A[row][col], A[row][~col] = A[row][~col], A[row][col]
    return A

def reflectMatrixHorz(A):
    for row in range(len(A) // 2):
        for col in range(len(A)):
            A[row][col], A[~row][col] = A[~row][col], A[row][col]
    return A

def reflectDiag(A):
    for i in range(len(A)):
        for j in range(0,i+1):
            A[i][j], A[j][i] =  A[j][i], A[i][j]
    return A

for row in reflectDiag(A):
    print (row)

for row in reflectDiag(B):
    print (row)
