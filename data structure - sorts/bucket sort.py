# for bucket sort we need another sort functionality
def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
    return A


A = [15, 13, 17, 89, 1, 3, 4, 2, 56, 12, 89, 75, 1, 5]


def bucket_sort(A):
    B = [[] for i in range(10)]
    for i in A:
        B[i//10] += [i]
    print(B)
    A = []
    for i in range(10):
        A += bubble_sort(B[i])

    print(A)


bucket_sort(A)
