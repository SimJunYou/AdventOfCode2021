coords = []
folds = []

def v_add(top, bottom):
    if len(top) >= len(bottom):
        for y in range(len(bottom)):
            for x in range(len(bottom[0])):
                top[y][x] |= bottom[::-1][y][x]
        return top
    else:
        for y in range(len(top)):
            for x in range(len(top[0])):
                bottom[::-1][y][x] |= top[y][x]
        return bottom

with open('test.in', 'r') as f:
    arr = f.readlines()
    for line in arr:
        line = line.strip()
        if line == '':
            continue
        elif 'fold along' in line:
            folds.append(line[11:])
        else:
            coords.append(tuple(map(int, line.split(','))))
    max_x, max_y = 0, 0
    for x,y in coords:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    matrix = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    print(max_x, max_y)
    for x,y in coords:
        matrix[y][x] = 1

    current_dir = 'v'
    for fold in folds:
        print(f"folding on {fold}")
        dirc, num = fold.split('=')
        num = int(num)
        if dirc == 'y':
            if current_dir == 'h':
                matrix = [list(x) for x in zip(*matrix)]
            matrix = v_add(matrix[:num], matrix[num+1:])
            current_dir = 'v'
        else:
            if current_dir == 'v':
                matrix = [list(x) for x in zip(*matrix)]
            matrix = v_add(matrix[:num], matrix[num+1:])
            current_dir = 'h'

    for line in matrix:
        for char in line:
            print(' ' if not char else '#', end='')
        print()


    

            

