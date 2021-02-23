A = [1, 2, 1, 3, 1, 5, 3, 4, 1, 2, 3, 0, 0,
     3, 0, 1, 0, 1, 2, 1, 2, 3, 1, 4, 1, 0]

n = len(A)
m = max(A)
c = [0]*(m+1)
print(c)
for i in A:
    c[i] += 1
print(c)

k = 0

for i in range(m+1):
    for j in range(c[i]):
        A[k], k = i, k+1

print(A)
# another method for counting sort need python ability

B = [1, 2, 1, 3, 1, 5, 3, 4, 1, 2, 3, 0, 0,
     3, 0, 1, 0, 1, 2, 3, 2, 5, 4, 5, 4, 1, 0, 3 ,1, 2, 3, 1, 4, 1, 0]

m = max(B)
n = len(B)
c = [0]*(m+1)
print(c)
for i in B:
    c[i] += 1
print(c)

B = []

for i in range(m+1):
    B += [i] * c[i]

print(B)
