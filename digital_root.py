def digital_root(number):
    # arguments: number (int)

    number_str = str(number)

    # Base case
    if len(number_str) == 1:
        return number

    int_sum = 0
    for digit_str in number_str:
        int_sum += int(digit_str)

    return digital_root(int_sum)

    #sum_str = str(int_sum)
    #len_sum = len(sum_str)
