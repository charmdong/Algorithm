def adder(a, b):
    return sum(range(a,b+1)) if a<b else sum(range(b,a+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(-3, -3))