with open('test.in', 'r') as f:
    arr = f.readlines()
    arr = [x.strip() for x in arr]
    oxy = arr.copy()
    co2 = arr.copy()

    index = 0
    while len(oxy) > 1:
        halfLength = len(oxy) // 2
        isOdd = len(oxy) % 2
        bitSequence = [int(x[index]) for x in oxy]
        if sum(bitSequence) == halfLength and not isOdd:
            mostCommonBit = '1'
        elif sum(bitSequence) > halfLength:
            mostCommonBit = '1'
        else:
            mostCommonBit = '0'
        oxy = [x for x in oxy if x[index] == mostCommonBit]
        index += 1
        print(index-1, oxy)
    
    index = 0
    print(index-1, co2)
    while len(co2) > 1:
        halfLength = len(co2) // 2
        isOdd = len(co2) % 2
        bitSequence = [int(x[index]) for x in co2]
        if sum(bitSequence) == halfLength and not isOdd:
            leastCommonBit = '0'
        elif sum(bitSequence) > halfLength:
            leastCommonBit = '0'
        else:
            leastCommonBit = '1'
        co2 = [x for x in co2 if x[index] == leastCommonBit]
        index += 1
        print(index-1, co2)

print(int(oxy[0], base=2), int(co2[0], base=2))
print(int(oxy[0], base=2) * int(co2[0], base=2))
