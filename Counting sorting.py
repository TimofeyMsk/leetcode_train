A = [3, 0, 0, 2, 3, 0, 1, 3, 3, 2]
C = [0]*4
for i, x in enumerate(A):
    C[x] += 1
for i in range(1, 4):
    C[i] = C[i-1] + C[i]
B = [0]*len(A)
for i in range(len(A)-1, -1, -1):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]
print(B)
