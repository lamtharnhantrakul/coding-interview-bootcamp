import sys

def computeNumPaths(n):
    path_dict = {}

    def computeHelper(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in path_dict.keys():
            return path_dict[n]
        else:
            path_dict[n] = computeHelper(n-1) + computeHelper(n-2) + computeHelper(n-3)
            return path_dict[n]
    return computeHelper(n)

print(computeNumPaths(int(sys.argv[1])))
