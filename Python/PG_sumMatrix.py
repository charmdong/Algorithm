def sumMatrix(A, B):
    answer = []
    size = len(A)
    size2 = len(A[0])
    for i in range(size) :
        tmp =[]
        for j in range(size2):
            tmp.append(A[i][j] + B[i][j])
        answer.append(tmp)

    return answer


print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

