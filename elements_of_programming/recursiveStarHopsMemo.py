import sys
def computeHops(n):
    hop_list = [1,2,3]
    result = []
    path_sum_dict = {i:0 for i in hop_list}

    def recursiveHops(path_list):
        path_sum = path_sum_dict[tuple(path_list)]
        print(path_list, path_sum)
        if path_sum < n and (n - path_sum) in hop_list:
            updated_path = path_list + [n - path_sum]
            results.append(updated_path)
            return
        else:
            for i in hop_list:
                updated_path = path_list + [i]
                path_sum_dict[tuple(updated_path)] = path_sum_dict[tuple(path_list)] + i
                recursiveHops(path_list)

    #edge case
    if n in hop_list:
        result.append([n])
    else:
        recursiveHops([])

    return result


num = int(sys.argv[1])
#print(num)
print(computeHops(num))
