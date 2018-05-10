def sumDivisor(num):
    answer = 0
    for i in range(num):
        if num%(i+1) == 0:
            answer += num//(i+1)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))


