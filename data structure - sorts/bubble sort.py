A = [3,1,2,4,1,2,5,23,756,43,674,23,7,137,1,123]

n = len(A)
for i in range(n-1):
    for j in range(n-1 , i , -1):
        if A[j-1] > A[j]:
            A[j-1] , A[j] = A[j] , A[j-1]
    print(A)