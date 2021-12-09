with open('test.in', 'r') as f:
    arr = f.readlines()
    length = len(arr)

    oxygen = ""
    index = 0
    while True:
        counter = 0
        tempArr = [n for n in arr if oxygen == n[:len(oxygen)]]
        for each in tempArr:
            counter += int(each.strip()[index])
        index += 1
        oxygen += str(int(counter >= len(tempArr) // 2))
        if len(tempArr) <= 1:
            oxygen_val = int(oxygen, 2)
            break

    co2 = ""
    index = 0
    while True:
        counter = 0
        tempArr = [n for n in arr if co2 == n[:len(co2)]]
        for each in tempArr:
            counter += int(each.strip()[index])
        index += 1
        co2 += str(int(counter < len(tempArr) // 2))
        if len(tempArr) <= 1:
            co2_val = int(co2, 2)
            break

print(oxygen, co2)
print(oxygen_val * co2_val)
        
