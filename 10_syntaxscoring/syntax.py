scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
match =  {'(': ')', '[': ']', '{': '}', '<': '>'}

with open('test.in', 'r') as f:
    stack = []
    arr = f.readlines()
    total = 0
    for line in arr:
        line = line.strip()
        for char in line:
            if char in ('(', '{', '[', '<'):
                stack.append(char)
            else:
                top = stack.pop()
                if match[top] != char:
                    total += scores[char]
    print(total)

            
