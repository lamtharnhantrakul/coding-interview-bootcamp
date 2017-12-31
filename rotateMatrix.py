a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def rotateImageC(a):
    a = zip(*reversed(a))
    a = [list(item) for item in a]
    return a

def rotateImageCC(a):
    a = zip(*a)
    a = [list(item) for item in a]
    a.reverse()
    return a

print(rotateImageCC(a))
