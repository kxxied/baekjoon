n_list = []

for _ in range(10):
    n = int(input())
    n_list.append(n % 42)

r = set(n_list)
print(len(r))