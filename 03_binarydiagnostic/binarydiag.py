with open('test.in', 'r') as f:
    arr = f.readlines()
    counter = [0] * len(arr[0].strip())
    for eachBin in arr:
        for index, eachNum in enumerate(eachBin.strip()):
            counter[index] += int(eachNum)
    print(counter)
    gamma = sum([2**i for i, n in enumerate(counter[::-1]) if n > len(arr)/2])
    epsilon = (2**len(counter) - 1) - gamma
print(gamma * epsilon)
        
