n = int(input())
n_list = list(map(int, input().split()))
m = max(n_list)

sum_list = []
for score in n_list:
    sum_list.append(score/m * 100)

avg = sum(sum_list)/n
print(avg)