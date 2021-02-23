A = [15, 13, 17, 89, 1, 3, 4, 2, 56, 12, 89, 75, 1, 5]

# i indicates how many items were sorted
for i in range(len(A)-1):
    min_index = i
    for j in range(i+1, len(A)):
        if A[j] < A[min_index]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]
print(A)
