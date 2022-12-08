n_list = [i for i in range(1, 31)]

for _ in range(28):
    x = int(input())
    n_list.remove(x)

print(min(n_list))
print(max(n_list))