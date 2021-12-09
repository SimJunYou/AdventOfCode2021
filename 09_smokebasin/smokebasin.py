with open('test.in', 'r') as f:
    heightmap = []
    height = 0
    for line in f.readlines():
        height += 1
        line = line.strip()
        heightmap.append([10] + list(map(int, line)) + [10])
    length = len(heightmap[0]) - 2
    buffer = len(heightmap[0]) * [10]
    heightmap = [buffer] + heightmap + [buffer]
    count = 0
    for x in range(1, length+1):
        for y in range(1, height+1):
            if heightmap[y][x] < heightmap[y+1][x] and\
               heightmap[y][x] < heightmap[y][x+1] and\
               heightmap[y][x] < heightmap[y-1][x] and\
               heightmap[y][x] < heightmap[y][x-1]:
                count += 1 + heightmap[y][x] 
    print(count)
