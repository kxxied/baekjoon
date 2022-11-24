while True:
     A, B = map(int, input().split())
     if 0 <= A and B < 10000:
         break

print(A + B)
print(A - B)
print(A * B)
print(int(A / B))
print(A % B)