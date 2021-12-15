import copy

def dijkstra(maze):
    minrisk = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
    minrisk[0][0] = [0]

    path = [[[] for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path[0][0] = [(0,0)]

    visited = set()
    queue = [(0,0)]

    debug = False 
    expectedVisited = len(maze) * len(maze[0])
    while len(visited) < expectedVisited:
        curr = queue.pop(0)
        x, y = curr
        if debug:
            print("current is", curr)
        
        neighbours = []
        # only need to consider right and bottom neighbour
        for xo, yo in ((1, 0), (0, 1)):
            # skip if visited already
            if (x+xo, y+yo) in visited:
                continue
            # append neighbours if within range and both offsets not the same 
            if len(maze[0]) > x+xo and len(maze) > y+yo:
                # one of the offsets must be 0 for right/bottom neighbour
                if (xo == 0) != (yo == 0):
                    neighbours.append((x+xo, y+yo))
        if debug:
            print("neighbours are", neighbours)

        # update minrisk
        for xn, yn in neighbours:
            if minrisk[xn][yn] == float('inf') or sum(minrisk[xn][yn]) > sum(minrisk[x][y]) + maze[xn][yn]:
                minrisk[xn][yn] = minrisk[x][y] + [maze[xn][yn]]
                path[xn][yn] = path[x][y] + [(xn,yn)]

        visited.add(curr)
        for each in neighbours:
            if each not in queue:
                queue.append(each)
        if debug:
            print("we have visited", len(visited), "nodes")

    return minrisk, path

def mazeprep(maze):
    newMaze = []
    origY, origX = len(maze), len(maze[0])
    for y in range(len(maze)*5):
        newMaze.append([])
        for x in range(len(maze[0])*5):
            adder = (x//origX) + (y//origY)
            newVal = maze[y%origY][x%origX] + adder
            if newVal > 9:
                newVal -= 9
            newMaze[-1].append(newVal)
    return newMaze

with open('test2.in', 'r') as f:
    arr = f.readlines()
    maze = []
    for line in arr:
        maze.append(list(map(int, line.strip())))

    newMaze = mazeprep(maze)
    '''
    for line in newMaze:
        print(''.join(map(str, line)))
    '''
    minrisk, path = dijkstra(newMaze)
    print(minrisk[-1][-1])
    print(sum(minrisk[-1][-1]))
    for x in range(len(minrisk)):
        for y in range(len(minrisk[0])):
            if (x,y) in path[-1][-1]:
                print('# ', end='')
            else:
                print('. ', end='')
        print()



