def number_generator(x, n):
    return list(range(x, x*n+1, x))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(2,5))