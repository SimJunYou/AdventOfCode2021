with open('test.in', 'r') as f:
    fwd, dep = 0, 0

    for each in f.readlines():
        direction, units = each.split()
        if direction[0] == 'd':
            dep += int(units)
        elif direction[0] == 'u':
            dep -= int(units)
        else:
            fwd += int(units)

print(fwd * dep)

