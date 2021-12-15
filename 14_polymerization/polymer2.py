from collections import Counter

with open('test.in', 'r') as f:
    arr = f.readlines()
    original = arr[0].strip()
    arr = arr[2:]
    pairs = dict()
    for pair in arr:
        key, val = pair.strip().split(' -> ')
        pairs[key] = val
   
    newPairs = dict()
    pairCounters = dict()
    for pair in pairs:
        print('working on', pair)
        template = pair
        for _ in range(20):
            newTemplate = ''
            for i in range(len(template)-1):
                c1, c2 = template[i], template[i+1]
                newTemplate += c1
                if c1+c2 in pairs.keys():
                    newTemplate += pairs[c1+c2]
            newTemplate += c2
            template = newTemplate
        newPairs[pair] = template
        pairCounters[pair] = Counter(template[1:])
        print('done! length is', len(template))
        print('counter is', pairCounters[pair])
        
    newString = original[0]
    for i in range(len(original)-1):
        print('making new string from', newString[i:i+2])
        newString += newPairs[original[i:i+2]][1:]
    print('new string length is', len(newString))
    counter = Counter(newString[0])
    num = 0
    for i in range(len(newString)-1):
        counter += pairCounters[newString[i:i+2]]
        num += 1
        if num % 10000000 == 0:
            print(num)

    print(counter)
    print(counter[max(counter, key=counter.get)] - counter[min(counter, key=counter.get)])
    
