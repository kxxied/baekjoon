A = input()
B = input()

A = int(A)
B1 = int(B[0])
B2 = int(B[1])
B3 = int(B[2])

print(A*B3, A*B2, A*B1, sep='\n')
print((A*B1)*100+(A*B2)*10+(A*B3))