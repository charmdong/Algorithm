def sum_digit(number):
    return sum(list(map(lambda x: int(x), list(str(number)))))




# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));