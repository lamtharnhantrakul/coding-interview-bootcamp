def reverseString(s,start_idx,end_idx):
    while start_idx < end_idx:
        s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
        start_idx, end_idx = start_idx + 1, end_idx - 1

def reverseWords(s):
    # reverse the string first
    s = "".join(reversed(s))

    start_idx = 0
    while True:
        end_idx = s.find(' ', start_idx)  # look for the white space separating the words
        if end_idx < 0: # we are at the end, so there is no white space to find
            break
        reverseString(s, start_idx, end_idx-1) # do not swap the white space
        start_idx = end_idx + 1 # skip the white space

    reverseString(s, start_idx, len(s)-1)
    return s

def reverse(s):
    rev = s.split(' ')
    return ' '.join(reversed(rev))

print(reverse('music is so cool!'))
