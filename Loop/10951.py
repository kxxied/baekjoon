while True:
    try:
        a, b = map(int, input().split())
        if 0 > a and b > 10:
            break
    except:
        break
    print(a+b)