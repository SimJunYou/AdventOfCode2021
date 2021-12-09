import statistics

memo = dict()

def getcost(arr, pos):
    if pos in memo.values():
        return memo[pos]
    diffArr = [abs(x-pos) for x in arr]
    costArr = [(diff*(1+diff))//2 for diff in diffArr]
    memo[pos] = sum(costArr)
    return memo[pos]

with open('test.in', 'r') as f:
    arr = list(map(int, f.readline().strip().split(',')))
    pos = statistics.median(arr)
    mid = getcost(arr, pos)
    while True:
        left = getcost(arr, pos-1)
        right = getcost(arr, pos+1)
        if mid < left and mid < right:
            break
        elif left < right:
            pos = pos - 1
            mid = left
        elif right < left:
            pos = pos + 1
            mid = right
    print(mid)


