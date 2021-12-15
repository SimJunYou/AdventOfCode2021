
def dijkstra(maze):
    minrisk = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
    minrisk[0][0] = 0

    visited = set()
    queue = [(0,0)]

    debug = True

    while len(visited) != len(maze[0]) * len(maze):
        curr = queue.pop(0)
        x, y = curr
        if debug:
            print("current is", curr)
        
        neighbours = []
        for xo in range(-1, 2):
            for yo in range(-1, 2):
                # skip if visited already
                if (x+xo, y+yo) in visited:
                    continue
                # append neighbours if within range and both offsets not the same 
                if len(maze[0]) > x+xo > -1 and len(maze) > y+yo > -1:
                    # one of the offsets must be 0 for 4 adjacent neighbours
                    if (xo == 0) != (yo == 0):
                        neighbours.append((x+xo, y+yo))
        if debug:
            print("neighbours are", neighbours)

        # update minrisk
        for xn, yn in neighbours:
            if minrisk[xn][yn] > minrisk[x][y] + maze[xn][yn]:
                minrisk[xn][yn] = minrisk[x][y] + maze[xn][yn]

        visited.add(curr)
        for each in neighbours:
            if each not in queue:
                queue.append(each)
        if debug:
            print("we have visited", len(visited), "nodes")
            print("queue is now", queue, "\n")
    return minrisk

with open('test2.in', 'r') as f:
    arr = f.readlines()
    maze = []
    for line in arr:
        maze.append(list(map(int, line.strip())))
    minrisk = dijkstra(maze)
    print(minrisk[-1][-1])



