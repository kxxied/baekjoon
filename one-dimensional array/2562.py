# n_list = [int(input()) for _ in range(9)]

n_list = []
for i in range(9):
    i = int(input())
    n_list.append(i)

print(max(n_list))
print(n_list.index(max(n_list))+1)