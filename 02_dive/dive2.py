with open('test.in', 'r') as f:
    fwd, dep, aim = 0, 0, 0

    for each in f.readlines():
        direction, units = each.split()
        if direction[0] == 'd':
            aim += int(units)
        elif direction[0] == 'u':
            aim -= int(units)
        else:
            fwd += int(units)
            dep += aim * int(units)

print(fwd * dep)

