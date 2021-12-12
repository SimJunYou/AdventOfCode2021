import statistics
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}
match =  {'(': ')', '[': ']', '{': '}', '<': '>'}

with open('test.in', 'r') as f:
    arr = f.readlines()
    total = 0
    scoreList = []
    for line in arr:
        line = line.strip()
        stack = [] 
        skipCurrent = False
        for char in line:
            if char in ('(', '{', '[', '<'):
                stack.append(char)
            else:
                top = stack.pop()
                if match[top] != char:
                    skipCurrent = True
                    break
        if skipCurrent:
            continue

        if len(stack) > 0:
            incompletescore = 0
            for char in stack[::-1]:
                incompletescore *= 5
                incompletescore += scores2[char]
            scoreList.append(incompletescore)
    print(statistics.median(scoreList))

            
