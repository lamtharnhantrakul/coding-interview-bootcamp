def int_to_string(x):
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    string = ''

    while True:
        string = str(x % 10) + string
        x = x//10
        if x == 0:
            break
    if is_negative:
        string = '-' + string

    return string

def int_to_string2(x):
    '''
    appending to the front of a string is inefficient,
    better to append to the back as an array and then join() and reverse
    '''

    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    string_array = []

    while x!=0:
        string_array.append(str(x%10))
        x = x//10

    string = ''.join(reversed(string_array))

    if is_negative:
        string = '-' + string

    return string

def int_to_string3(x):
    '''
    reference solution
    '''
    is_negative = False
    if x < 0:
        x, is_negative = -x, True  # the `-x` is like `abs(x)`

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int1(string):
    result = 0
    for i, char in enumerate(reversed(string)):
        if char == '-':
            result = -result
            break
        result += (int(char) * (10**i))
    return result

def string_to_int2(string):
    '''
    more efficient method is going from the front to the back
    '''
    r = 0
    is_negative = False
    for char in string:
        if char == '-':
            is_negative = True
        else:
            r = (r*10) + int(char) # here we multiply by constant of 10.
    return (-r if is_negative else r)



print(string_to_int2('314'))
print(string_to_int2('-314'))
