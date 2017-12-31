def convert_base(num_int, b1, b2):
    hexdigits = '0123456789ABCDEF'

    # convert from b1 to decimal
    num_dec = 0
    counter = 0

    while True:
        num_dec += (num_int % 10)*(b1**counter)  # extract last digit and multiply by base
        num_int //= 10 # remove the last digit for next iteration
        counter += 1
        if num_int == 0:
            # we have completed working through all digits
            break

    # convert from decimal to b2
    string_num = ''
    while True:
        string_num = str(hexdigits[num_dec % b2]) + string_num
        num_dec //= b2
        if num_dec == 0:
            # we have completed working through all digits
            break

    return string_num
print(convert_base(615,7,13))
