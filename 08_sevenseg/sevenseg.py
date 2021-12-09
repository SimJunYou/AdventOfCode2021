def unscramble(words):
    sets = {i: set() for i in range(10)}
    set5a, set5b, set5c = set(), set(), set()
    set6a, set6b, set6c = set(), set(), set()
    for w in words:
        if len(w) == 2:
            sets[1] = set(w)
        elif len(w) == 3:
            sets[7] = set(w)
        elif len(w) == 4:
            sets[4] = set(w)
        elif len(w) == 5:
            if not set5a:
                set5a = set(w)
            elif set(w) != set5a and not set5b:
                set5b = set(w)
            elif set(w) != set5a and set(w) != set5b and not set5c:
                set5c = set(w)
        elif len(w) == 6:
            if not set6a:
                set6a = set(w)
            elif set(w) != set6a and not set6b:
                set6b = set(w)
            elif set(w) != set6a and set(w) != set6b and not set6c:
                set6c = set(w)
        elif len(w) == 7:
            sets[8] = set(w)
    
    bottomLeft = sets[8] - (sets[4] | sets[7])
    top = sets[7] - sets[1]

    # out of 5a, 5b, and 5c, one is 2, one is 3, and one is 5
    if len(set5a & sets[1]) == 2:
        # set5a is 3
        sets[3] = set5a
        set5x, set5y = set5b, set5c
    elif len(set5b & sets[1]) == 2:
        # set5b is 3
        sets[3] = set5b
        set5x, set5y = set5a, set5c
    else:
        sets[3] = set5c
        set5x, set5y = set5a, set5b

    # set5x and set5y are either 2 or 5
    if len(set5x & sets[4]) == 3:
        # set5x is 5
        sets[5] = set5x
        sets[2] = set5y
    else:
        sets[2] = set5x
        sets[5] = set5y

    # out of 6a, 6b, and 6c, one is 6, one is 9, and one is 0
    if len(set6a & sets[4]) == 4:
        # set6a is 9
        sets[9] = set6a
        set6x, set6y = set6b, set6c
    elif len(set6b & sets[4]) == 4:
        # set6b is 9
        sets[9] = set6b
        set6x, set6y = set6a, set6c
    else:
        sets[9] = set6c
        set6x, set6y = set6a, set6b

    # out of 6x and 6y, one is 6 and one is 0
    if len(set6x & sets[7]) == 2:
        # set6x is 6
        sets[6] = set6x
        sets[0] = set6y
    else:
        sets[0] = set6x
        sets[6] = set6y

    return sets

def decode(wordSeq, ref):
    output = ''
    for word in wordSeq:
        for num, chars in ref.items():
            if chars == set(word):
                output += str(num)
                break
    return int(output)

with open('test.in', 'r') as f:
    total = 0
    for eachLine in f.readlines():
        inword, outword = eachLine.split(' | ')
        inword, outword = inword.split(), outword.strip().split()
        ref = unscramble(inword + outword)
        total += decode(outword, ref)
    print(total)
