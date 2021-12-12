adj = dict()
count = 0
paths = []

def dfs(path, twice, curr):
    global adj, count, paths, small_visited
    if path == 'start,A,b,A,c,A':
        print(path, twice, curr)
    
    if curr == "end":
        count += 1
        paths.append(path)
        return
    
    neighbours = adj[curr]
    for each in neighbours:
        newTwice = twice
        if each == 'start':
            continue
        if each == each.lower() and each in path:
            if twice:
                continue
            newTwice = True
        newPath = path + f",{each}"
        dfs(newPath, newTwice, each)


with open('test.in', 'r') as f:
    for line in f.readlines():
        x, y = line.strip().split('-')
        if x not in adj.keys():
            adj[x] = [y]
        else:
            adj[x].append(y)
        if y not in adj.keys():
            adj[y] = [x]
        else:
            adj[y].append(x)
    dfs("start", False, "start")
    #for each in sorted(paths):
    #    print(each)
    print(count)


    
