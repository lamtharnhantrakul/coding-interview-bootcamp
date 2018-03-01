import sys

def computeHops(n):
    hop_choices = [1,2,3]
    result = []
    path_dict = {}

    def recursiveHops(arr):

        print(arr,n - sum(arr))

        if tuple(arr)in path_dict.keys() and sum(arr) < n:
            # base case
            if (n - sum(arr)) in hop_choices:
                new_arr = arr + [n - sum(arr)]
                result.append(new_arr)
                path_dict[tuple(arr)] = new_arr
                return
            # only continue if sum is less than n, otherwise this will be an infinite loop
            for i in hop_choices:
                recursiveHops(arr + [i])
        else:
            return path_dict[tuple(arr)]
    # edge case
    if n in hop_choices:
        result.append([n])
    else:
        recursiveHops([])

    return result

num = int(sys.argv[1])
#print(num)
print(computeHops(num))
