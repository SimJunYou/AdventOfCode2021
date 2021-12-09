def checkWinner(board, nums):
    check = [1 if x in nums else 0 for x in board]
    for i in range(5):
        if sum(check[i*5:i*5+5]) == 5:
            return check
        if sum(check[i*5::5]) == 5:
            return check
    return False

with open('test.in', 'r') as f:
    arr = f.readlines()
    nums = list(map(int, arr[0].split(',')))
    bingo_cards = []
    index = -1
    for each in arr[1:]:
        if len(each) < 2:
            index += 1
            bingo_cards.append([])
            continue
        bingo_cards[index] += list(map(int, each.split()))

    alreadyWon = []
    for i in range(1, len(nums)):
        current = nums[0:i]
        winner = False
        for index, eachCard in enumerate(bingo_cards):
            if index in alreadyWon:
                continue
            elif checkWinner(eachCard, current):
                if len(alreadyWon) == len(bingo_cards) - 1:
                    winner = eachCard
                    break
                else:
                    alreadyWon.append(index)
        if winner:
            break
    check = checkWinner(winner, current)
    total = 0
    for num, dont_include in zip(winner, check):
        total += 0 if dont_include else num 
    print(total * current[-1])

