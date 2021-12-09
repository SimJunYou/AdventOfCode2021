with open('test.in', 'r') as f:
    arr = f.readlines()
    arr = [x.strip().split(' -> ') for x in arr]
    arr = [tuple([tuple(map(int, y.split(','))) for y in x]) for x in arr]

    maxX, maxY = 0, 0
    for eachLine in arr:
        for eachSide in eachLine:
            x, y = eachSide
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y

    counter = [[0 for _ in range(maxX+1)] for _ in range(maxY+1)]
    
    for eachLine in arr:
        left, right = eachLine
        xl, yl = left
        xr, yr = right
        
        if yl != yr and xl != xr:
            continue
        
        elif yl != yr:
            if yl < yr:
                for i in range(yl, yr+1):
                    counter[i][xl] += 1
            else:
                for i in range(yr, yl+1):
                    counter[i][xl] += 1
        
        else:
            if xl < xr:
                for i in range(xl, xr+1):
                    counter[yl][i] += 1
            else:
                for i in range(xr, xl+1):
                    counter[yl][i] += 1

    total = 0
    for eachRow in counter:
        for eachNum in eachRow:
            if eachNum > 1:
                total += 1
    print(total)
