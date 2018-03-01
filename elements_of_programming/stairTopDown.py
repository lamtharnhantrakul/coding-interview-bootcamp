import sys
def computeNumHopPaths(n):

    # don't go beyond n
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return computeNumHopPaths(n-1) + computeNumHopPaths(n-2) + computeNumHopPaths(n-3)

print(computeNumHopPaths(int(sys.argv[1])))
