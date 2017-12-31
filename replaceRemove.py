def removeElement(string, char):
    w_idx = 0
    for i in range(len(string)):
        if string[i] != char:
            string[w_idx] = string[i]
            w_idx += 1

    # O(n) TIME and O(1) SPACE

    return string

print(removeElement(list('hannnnnnoi       '),'n'))
