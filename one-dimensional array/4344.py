c = int(input())

for _ in range(c):
    test_case = list(map(int, input().split()))
    n = test_case[0]

    test_case.pop(0)
    avg = sum(test_case) / n

    stu = 0
    for score in test_case:
        if score > avg:
            stu += 1
        else:
            continue

    print('{:.3f}'.format(stu / n * 100) + '%')
