with open('test.in') as f:
    prev = -1
    count = 0
    for each in f.readlines():
        if prev == -1:
            prev = int(each)
        else:
            curr = int(each)
            if curr > prev:
                count += 1
            prev = curr
print(count)
