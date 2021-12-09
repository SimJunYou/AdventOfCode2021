def recolor(old, new, unionmap):
    for i in range(len(unionmap)):
        unionmap[i] = [new if x == old else x for x in unionmap[i]]
    return unionmap

with open('test.in', 'r') as f:
    heightmap = []
    unionmap = []
    height = 0
    for line in f.readlines():
        height += 1
        line = line.strip()
        heightmap.append(list(map(int, line)))
        unionmap.append([0] * len(heightmap[0]))
    length = len(heightmap[0])
    unique = 1
    for y in range(height):
        for x in range(length):
            if heightmap[y][x] != 9: 
                topColored = (unionmap[y-1][x] != 0) if y > 0 else False
                leftColored = (unionmap[y][x-1] != 0) if x > 0 else False
                if topColored and leftColored:
                    old, new = unionmap[y-1][x], unionmap[y][x-1]
                    unionmap = recolor(old, new, unionmap)
                    unionmap[y][x] = new
                elif topColored:
                    unionmap[y][x] = unionmap[y-1][x]
                elif leftColored:
                    unionmap[y][x] = unionmap[y][x-1]
                else:
                    unionmap[y][x] = unique
                    unique += 1
            '''
            for lst in (heightmap, unionmap):
                for eachRow in lst:
                    print(''.join(map(str,eachRow)))
                print()
            '''

    sizeDict = dict()
    for row in unionmap:
        for color in row:
            if color == 0:
                continue
            if color in sizeDict.keys():
                sizeDict[color] += 1
            else:
                sizeDict[color] = 1

    print(sizeDict)
    top3 = sorted(list(sizeDict.values()))[-3:]
    print(top3)
    prod = 1
    for each in top3:
        prod *= each
    print(prod)


        
