def sumMatrix(A,B):
    answer = A
    for j in range(len(answer)):
        for i in range(len(answer[0])):
            answer[j][i] = A[j][i] + B[j][i]
    return answer

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
