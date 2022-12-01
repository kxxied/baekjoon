H, M = map(int, input().split())
timer = int(input())

M += timer

H = (H + M // 60) % 24
M = M % 60

print(H, M)