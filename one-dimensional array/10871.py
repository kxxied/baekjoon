a, x = map(int, input().split())
x_list = list(map(int, input().split()))

for i in range(a):
    if x_list[i] < x:
        print(x_list[i], end=' ')