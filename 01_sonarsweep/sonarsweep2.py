with open('test.in', 'r') as f:
    bck, fwd = 0, 3
    arr = f.readlines()
    length = len(arr)
    count = 0

    while fwd < length:
        if int(arr[fwd]) > int(arr[bck]):
            count += 1
        bck += 1
        fwd += 1
print(count)
