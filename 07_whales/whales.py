import statistics

with open('test.in', 'r') as f:
    arr = list(map(int, f.readline().strip().split(',')))
    median = int(statistics.median(arr))
    total = sum([abs(x - median) for x in arr])
    print(total)
