n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
    # print('{0:>{1}}'.format(('*' * i), n))
    # print('{star:>{n}}'.format(star=('*' * i), n=n))
    # print(('*'*i).rjust(n))