n = int(input())

for _ in range(n):
    testCase = input()
    score, sum_score = 0, 0

    for q in testCase:
        if q == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
