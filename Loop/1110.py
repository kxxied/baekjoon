n = int(input())
org_n = n
cnt = 0

while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    n = (b * 10) + c

    cnt += 1
    if org_n == n:
        break

print(cnt)