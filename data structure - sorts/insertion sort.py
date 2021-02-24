A =  [67, 65, 17, 4, 3, 2, 1]
# [2,3,1,65,4,17,67]
ops = 0
for i in range(1 , len(A)):
    temp = A[i]
    j = i - 1
    # ops += 1
    while j >= 0 and A[j] > temp:
        ops += 1
        A[j+1] = A[j]
        j -= 1
    A[j+1] = temp
print(A)
print(ops)
