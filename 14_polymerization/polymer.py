from collections import Counter

with open('test.in', 'r') as f:
    arr = f.readlines()
    template = arr[0].strip()
    arr = arr[2:]
    pairs = dict()
    for pair in arr:
        key, val = pair.strip().split(' -> ')
        pairs[key] = val
    
    for _ in range(40):
        newTemplate = ''
        for i in range(len(template)-1):
            c1, c2 = template[i], template[i+1]
            newTemplate += c1
            if c1+c2 in pairs.keys():
                newTemplate += pairs[c1+c2]
        newTemplate += c2
        template = newTemplate

    counts = dict(Counter(template))
    print(counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)])
    
