with open('test.in', 'r') as f:
    days = [0 for _ in range(9)]
    for each in f.readline().strip().split(','):
        days[int(each)] += 1
    print(days)
    
    for _ in range(256):
        reproducing = days[0]
        days += [reproducing] # child fish
        days[7] += reproducing # parent fish
        days.pop(0)
    print(sum(days))


