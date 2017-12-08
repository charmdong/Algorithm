def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));